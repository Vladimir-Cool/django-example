from django.contrib import admin


from .models import BotSetting, MessageSetting, ChatSetting


@admin.register(BotSetting)
class BotSettingAdmin(admin.ModelAdmin):
    list_display = 'id', 'name'
    list_display_links = 'id', 'name'


@admin.register(MessageSetting)
class MessageSettingAdmin(admin.ModelAdmin):
    list_display = 'id', 'name', 'bot', 'chat'
    list_display_links = 'id', 'name'

    # @admin.display
    # def get_bot_setting_name(self, obj):
    #     print(obj.bot.name)
    #     return obj.bot.name


@admin.register(ChatSetting)
class ChatSettingAdmin(admin.ModelAdmin):
    list_display = 'id', 'name'
    list_display_links = 'id', 'name'

