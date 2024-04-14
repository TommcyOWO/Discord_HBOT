import discord
# from mod.dms.dm_sqlite import create_table,update_added_members
from mod.dms.dm_mongo import add_member, fetch_data
class add_data(discord.ui.Modal,title="建立共享"):
    add_member = discord.ui.TextInput(
        label='新增成員',
        placeholder='Discord NAME',
    )
    
    async def on_submit(self,interaction: discord.Interaction):
        try:
            # update_added_members(interaction.user.id,int(self.add_member.value))
            add_member(interaction.user.display_name,self.add_member.value,1)
            embed = interaction.message.embeds[0]
            embed.set_footer(text=f'成功添加 {self.add_member.value}')
            await interaction.response.edit_message(embed=embed)
        except:
            embed = interaction.message.embeds[0]
            embed.set_footer(text=f'添加失敗')
            await interaction.response.edit_message(embed=embed)
            

class get_data(discord.ui.Modal,title="提取資料"):
    add_code = discord.ui.TextInput(
        label='共享代碼',
        placeholder='Discord ID',
    )
    
    async def on_submit(self,interaction: discord.Interaction):
        embed = interaction.message.embeds[0]
        state = fetch_data(int(self.add_code.value))
        embed.set_footer(text=state)
        await interaction.response.edit_message(embed=embed)