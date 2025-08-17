import discord
from discord.ext import commands
import random

class GamingCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="split", aliases=["紅白"])
    async def split_teams(self, ctx):
        """VC参加者を攻撃・防衛に分け、指定VCへ移動します"""
        config = self.bot.config
        excluded_ids = config.get("excluded_user_ids", [])
        vc = ctx.author.voice.channel if ctx.author.voice else None

        if not vc:
            await ctx.send("❌ VCに参加してから使ってください。")
            return

        members = [m for m in vc.members if not m.bot and m.id not in excluded_ids]
        if len(members) < 2:
            await ctx.send("⚠️ チーム分けには最低2人必要です。")
            return

        random.shuffle(members)
        mid = len(members) // 2
        team_attack = members[:mid]
        team_defense = members[mid:]

        attack_vc = discord.utils.get(ctx.guild.voice_channels, name=config.get("attack_channel_name"))
        defense_vc = discord.utils.get(ctx.guild.voice_channels, name=config.get("defense_channel_name"))

        for m in team_attack:
            if attack_vc:
                await m.move_to(attack_vc)
        for m in team_defense:
            if defense_vc:
                await m.move_to(defense_vc)

        embed = discord.Embed(title="⚔️ チーム分け完了！", color=discord.Color.dark_red())
        embed.add_field(name=f"🔥 攻撃（→ {attack_vc.name}）", value="\n".join(m.display_name for m in team_attack), inline=True)
        embed.add_field(name=f"🛡️ 防衛（→ {defense_vc.name}）", value="\n".join(m.display_name for m in team_defense), inline=True)
        embed.set_footer(text="GAME START!!!!!")
        await ctx.send(embed=embed)

    @commands.command(name="exclude", aliases=["除外"])
    @commands.has_permissions(administrator=True)
    async def exclude_user(self, ctx, member: discord.Member):
        """指定ユーザーを除外リストに追加します"""
        excluded = self.bot.config.get("excluded_user_ids", [])
        if member.id in excluded:
            await ctx.send(f"⚠️ {member.display_name} はすでに除外されています。")
            return

        excluded.append(member.id)
        self.bot.config["excluded_user_ids"] = excluded
        self.bot.save_config()
        await ctx.send(f"✅ {member.display_name} を除外リストに追加しました。")

    @commands.command(name="include", aliases=["除外解除"])
    @commands.has_permissions(administrator=True)
    async def include_user(self, ctx, member: discord.Member):
        """除外リストから指定ユーザーを復帰させます"""
        excluded = self.bot.config.get("excluded_user_ids", [])
        if member.id not in excluded:
            await ctx.send(f"⚠️ {member.display_name} は除外されていません。")
            return

        excluded.remove(member.id)
        self.bot.config["excluded_user_ids"] = excluded
        self.bot.save_config()
        await ctx.send(f"✅ {member.display_name} を除外リストから削除しました。")

    @commands.command(name="excluded", aliases=["除外リスト"])
    @commands.has_permissions(administrator=True)
    async def show_excluded(self, ctx):
        """現在の除外リストを表示します"""
        excluded_ids = self.bot.config.get("excluded_user_ids", [])
        if not excluded_ids:
            await ctx.send("📭 除外リストは空です。")
            return

        members = []
        for user_id in excluded_ids:
            member = ctx.guild.get_member(user_id)
            members.append(member.display_name if member else f"❓ Unknown ({user_id})")

        embed = discord.Embed(title="🚫 除外ユーザー一覧", color=discord.Color.orange())
        embed.description = "\n".join(members)
        await ctx.send(embed=embed)

# ✅ 非同期でCogを登録するように修正
async def setup(bot):
    await bot.add_cog(GamingCommands(bot))
