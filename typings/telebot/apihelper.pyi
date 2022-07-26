"""
This type stub file was generated by pyright.
"""

from telebot import types

logger = ...
proxy = ...
session = ...
API_URL = ...
FILE_URL = ...
CONNECT_TIMEOUT = ...
READ_TIMEOUT = ...
LONG_POLLING_TIMEOUT = ...
SESSION_TIME_TO_LIVE = ...
RETRY_ON_ERROR = ...
RETRY_TIMEOUT = ...
MAX_RETRIES = ...
RETRY_ENGINE = ...
CUSTOM_SERIALIZER = ...
CUSTOM_REQUEST_SENDER = ...
ENABLE_MIDDLEWARE = ...
def get_me(token):
    ...

def log_out(token):
    ...

def close(token):
    ...

def get_file(token, file_id):
    ...

def get_file_url(token, file_id): # -> str:
    ...

def download_file(token, file_path): # -> bytes:
    ...

def send_message(token, chat_id, text, disable_web_page_preview=..., reply_to_message_id=..., reply_markup=..., parse_mode=..., disable_notification=..., timeout=..., entities=..., allow_sending_without_reply=..., protect_content=...):
    """
    Use this method to send text messages. On success, the sent Message is returned.
    :param token:
    :param chat_id:
    :param text:
    :param disable_web_page_preview:
    :param reply_to_message_id:
    :param reply_markup:
    :param parse_mode:
    :param disable_notification:
    :param timeout:
    :param entities:
    :param allow_sending_without_reply:
    :param protect_content:
    :return:
    """
    ...

def set_webhook(token, url=..., certificate=..., max_connections=..., allowed_updates=..., ip_address=..., drop_pending_updates=..., timeout=..., secret_token=...):
    ...

def delete_webhook(token, drop_pending_updates=..., timeout=...):
    ...

def get_webhook_info(token, timeout=...):
    ...

def get_updates(token, offset=..., limit=..., timeout=..., allowed_updates=..., long_polling_timeout=...):
    ...

def get_user_profile_photos(token, user_id, offset=..., limit=...):
    ...

def get_chat(token, chat_id):
    ...

def leave_chat(token, chat_id):
    ...

def get_chat_administrators(token, chat_id):
    ...

def get_chat_member_count(token, chat_id):
    ...

def set_sticker_set_thumb(token, name, user_id, thumb):
    ...

def set_chat_sticker_set(token, chat_id, sticker_set_name):
    ...

def delete_chat_sticker_set(token, chat_id):
    ...

def get_chat_member(token, chat_id, user_id):
    ...

def forward_message(token, chat_id, from_chat_id, message_id, disable_notification=..., timeout=..., protect_content=...):
    ...

def copy_message(token, chat_id, from_chat_id, message_id, caption=..., parse_mode=..., caption_entities=..., disable_notification=..., reply_to_message_id=..., allow_sending_without_reply=..., reply_markup=..., timeout=..., protect_content=...):
    ...

def send_dice(token, chat_id, emoji=..., disable_notification=..., reply_to_message_id=..., reply_markup=..., timeout=..., allow_sending_without_reply=..., protect_content=...):
    ...

def send_photo(token, chat_id, photo, caption=..., reply_to_message_id=..., reply_markup=..., parse_mode=..., disable_notification=..., timeout=..., caption_entities=..., allow_sending_without_reply=..., protect_content=...):
    ...

def send_media_group(token, chat_id, media, disable_notification=..., reply_to_message_id=..., timeout=..., allow_sending_without_reply=..., protect_content=...):
    ...

def send_location(token, chat_id, latitude, longitude, live_period=..., reply_to_message_id=..., reply_markup=..., disable_notification=..., timeout=..., horizontal_accuracy=..., heading=..., proximity_alert_radius=..., allow_sending_without_reply=..., protect_content=...):
    ...

def edit_message_live_location(token, latitude, longitude, chat_id=..., message_id=..., inline_message_id=..., reply_markup=..., timeout=..., horizontal_accuracy=..., heading=..., proximity_alert_radius=...):
    ...

def stop_message_live_location(token, chat_id=..., message_id=..., inline_message_id=..., reply_markup=..., timeout=...):
    ...

def send_venue(token, chat_id, latitude, longitude, title, address, foursquare_id=..., foursquare_type=..., disable_notification=..., reply_to_message_id=..., reply_markup=..., timeout=..., allow_sending_without_reply=..., google_place_id=..., google_place_type=..., protect_content=...):
    ...

def send_contact(token, chat_id, phone_number, first_name, last_name=..., vcard=..., disable_notification=..., reply_to_message_id=..., reply_markup=..., timeout=..., allow_sending_without_reply=..., protect_content=...):
    ...

def send_chat_action(token, chat_id, action, timeout=...):
    ...

def send_video(token, chat_id, data, duration=..., caption=..., reply_to_message_id=..., reply_markup=..., parse_mode=..., supports_streaming=..., disable_notification=..., timeout=..., thumb=..., width=..., height=..., caption_entities=..., allow_sending_without_reply=..., protect_content=...):
    ...

def send_animation(token, chat_id, data, duration=..., caption=..., reply_to_message_id=..., reply_markup=..., parse_mode=..., disable_notification=..., timeout=..., thumb=..., caption_entities=..., allow_sending_without_reply=..., protect_content=..., width=..., height=...):
    ...

def send_voice(token, chat_id, voice, caption=..., duration=..., reply_to_message_id=..., reply_markup=..., parse_mode=..., disable_notification=..., timeout=..., caption_entities=..., allow_sending_without_reply=..., protect_content=...):
    ...

def send_video_note(token, chat_id, data, duration=..., length=..., reply_to_message_id=..., reply_markup=..., disable_notification=..., timeout=..., thumb=..., allow_sending_without_reply=..., protect_content=...):
    ...

def send_audio(token, chat_id, audio, caption=..., duration=..., performer=..., title=..., reply_to_message_id=..., reply_markup=..., parse_mode=..., disable_notification=..., timeout=..., thumb=..., caption_entities=..., allow_sending_without_reply=..., protect_content=...):
    ...

def send_data(token, chat_id, data, data_type, reply_to_message_id=..., reply_markup=..., parse_mode=..., disable_notification=..., timeout=..., caption=..., thumb=..., caption_entities=..., allow_sending_without_reply=..., disable_content_type_detection=..., visible_file_name=..., protect_content=...):
    ...

def get_method_by_type(data_type): # -> Literal['sendDocument', 'sendSticker'] | None:
    ...

def ban_chat_member(token, chat_id, user_id, until_date=..., revoke_messages=...):
    ...

def unban_chat_member(token, chat_id, user_id, only_if_banned):
    ...

def restrict_chat_member(token, chat_id, user_id, until_date=..., can_send_messages=..., can_send_media_messages=..., can_send_polls=..., can_send_other_messages=..., can_add_web_page_previews=..., can_change_info=..., can_invite_users=..., can_pin_messages=...):
    ...

def promote_chat_member(token, chat_id, user_id, can_change_info=..., can_post_messages=..., can_edit_messages=..., can_delete_messages=..., can_invite_users=..., can_restrict_members=..., can_pin_messages=..., can_promote_members=..., is_anonymous=..., can_manage_chat=..., can_manage_video_chats=...):
    ...

def set_chat_administrator_custom_title(token, chat_id, user_id, custom_title):
    ...

def ban_chat_sender_chat(token, chat_id, sender_chat_id):
    ...

def unban_chat_sender_chat(token, chat_id, sender_chat_id):
    ...

def set_chat_permissions(token, chat_id, permissions):
    ...

def create_chat_invite_link(token, chat_id, name, expire_date, member_limit, creates_join_request):
    ...

def edit_chat_invite_link(token, chat_id, invite_link, name, expire_date, member_limit, creates_join_request):
    ...

def revoke_chat_invite_link(token, chat_id, invite_link):
    ...

def export_chat_invite_link(token, chat_id):
    ...

def approve_chat_join_request(token, chat_id, user_id):
    ...

def decline_chat_join_request(token, chat_id, user_id):
    ...

def set_chat_photo(token, chat_id, photo):
    ...

def delete_chat_photo(token, chat_id):
    ...

def set_chat_title(token, chat_id, title):
    ...

def get_my_commands(token, scope=..., language_code=...):
    ...

def set_chat_menu_button(token, chat_id=..., menu_button=...):
    ...

def get_chat_menu_button(token, chat_id=...):
    ...

def set_my_default_administrator_rights(token, rights=..., for_channels=...):
    ...

def get_my_default_administrator_rights(token, for_channels=...):
    ...

def set_my_commands(token, commands, scope=..., language_code=...):
    ...

def delete_my_commands(token, scope=..., language_code=...):
    ...

def set_chat_description(token, chat_id, description):
    ...

def pin_chat_message(token, chat_id, message_id, disable_notification=...):
    ...

def unpin_chat_message(token, chat_id, message_id):
    ...

def unpin_all_chat_messages(token, chat_id):
    ...

def edit_message_text(token, text, chat_id=..., message_id=..., inline_message_id=..., parse_mode=..., entities=..., disable_web_page_preview=..., reply_markup=...):
    ...

def edit_message_caption(token, caption, chat_id=..., message_id=..., inline_message_id=..., parse_mode=..., caption_entities=..., reply_markup=...):
    ...

def edit_message_media(token, media, chat_id=..., message_id=..., inline_message_id=..., reply_markup=...):
    ...

def edit_message_reply_markup(token, chat_id=..., message_id=..., inline_message_id=..., reply_markup=...):
    ...

def delete_message(token, chat_id, message_id, timeout=...):
    ...

def send_game(token, chat_id, game_short_name, disable_notification=..., reply_to_message_id=..., reply_markup=..., timeout=..., allow_sending_without_reply=..., protect_content=...):
    ...

def set_game_score(token, user_id, score, force=..., disable_edit_message=..., chat_id=..., message_id=..., inline_message_id=...):
    """
    Use this method to set the score of the specified user in a game. On success, if the message was sent by the bot, returns the edited Message, otherwise returns True. Returns an error, if the new score is not greater than the user's current score in the chat.
    :param token: Bot's token (you don't need to fill this)
    :param user_id: User identifier
    :param score: New score, must be non-negative
    :param force: (Optional) Pass True, if the high score is allowed to decrease. This can be useful when fixing mistakes or banning cheaters
    :param disable_edit_message: (Optional) Pass True, if the game message should not be automatically edited to include the current scoreboard
    :param chat_id: (Optional, required if inline_message_id is not specified) Unique identifier for the target chat (or username of the target channel in the format @channelusername)
    :param message_id: (Optional, required if inline_message_id is not specified) Unique identifier of the sent message
    :param inline_message_id: (Optional, required if chat_id and message_id are not specified) Identifier of the inline message
    :return:
    """
    ...

def get_game_high_scores(token, user_id, chat_id=..., message_id=..., inline_message_id=...):
    """
    Use this method to get data for high score tables. Will return the score of the specified user and several of his neighbors in a game. On success, returns an Array of GameHighScore objects.
    This method will currently return scores for the target user, plus two of his closest neighbors on each side. Will also return the top three users if the user and his neighbors are not among them. Please note that this behavior is subject to change.
    :param token: Bot's token (you don't need to fill this)
    :param user_id: Target user id
    :param chat_id: (Optional, required if inline_message_id is not specified) Unique identifier for the target chat (or username of the target channel in the format @channelusername)
    :param message_id: (Optional, required if inline_message_id is not specified) Unique identifier of the sent message
    :param inline_message_id: (Optional, required if chat_id and message_id are not specified) Identifier of the inline message
    :return:
    """
    ...

def send_invoice(token, chat_id, title, description, invoice_payload, provider_token, currency, prices, start_parameter=..., photo_url=..., photo_size=..., photo_width=..., photo_height=..., need_name=..., need_phone_number=..., need_email=..., need_shipping_address=..., send_phone_number_to_provider=..., send_email_to_provider=..., is_flexible=..., disable_notification=..., reply_to_message_id=..., reply_markup=..., provider_data=..., timeout=..., allow_sending_without_reply=..., max_tip_amount=..., suggested_tip_amounts=..., protect_content=...):
    """
    Use this method to send invoices. On success, the sent Message is returned.
    :param token: Bot's token (you don't need to fill this)
    :param chat_id: Unique identifier for the target private chat
    :param title: Product name
    :param description: Product description
    :param invoice_payload: Bot-defined invoice payload, 1-128 bytes. This will not be displayed to the user, use for your internal processes.
    :param provider_token: Payments provider token, obtained via @Botfather
    :param currency: Three-letter ISO 4217 currency code, see https://core.telegram.org/bots/payments#supported-currencies
    :param prices: Price breakdown, a list of components (e.g. product price, tax, discount, delivery cost, delivery tax, bonus, etc.)
    :param start_parameter: Unique deep-linking parameter that can be used to generate this invoice when used as a start parameter
    :param photo_url: URL of the product photo for the invoice. Can be a photo of the goods or a marketing image for a service. People like it better when they see what they are paying for.
    :param photo_size: Photo size
    :param photo_width: Photo width
    :param photo_height: Photo height
    :param need_name: Pass True, if you require the user's full name to complete the order
    :param need_phone_number: Pass True, if you require the user's phone number to complete the order
    :param need_email: Pass True, if you require the user's email to complete the order
    :param need_shipping_address: Pass True, if you require the user's shipping address to complete the order
    :param is_flexible: Pass True, if the final price depends on the shipping method
    :param send_phone_number_to_provider: Pass True, if user's phone number should be sent to provider
    :param send_email_to_provider: Pass True, if user's email address should be sent to provider
    :param disable_notification: Sends the message silently. Users will receive a notification with no sound.
    :param reply_to_message_id: If the message is a reply, ID of the original message
    :param reply_markup: A JSON-serialized object for an inline keyboard. If empty, one 'Pay total price' button will be shown. If not empty, the first button must be a Pay button
    :param provider_data: A JSON-serialized data about the invoice, which will be shared with the payment provider. A detailed description of required fields should be provided by the payment provider.
    :param timeout:
    :param allow_sending_without_reply:
    :param max_tip_amount: The maximum accepted amount for tips in the smallest units of the currency
    :param suggested_tip_amounts: A JSON-serialized array of suggested amounts of tips in the smallest units of the currency.
        At most 4 suggested tip amounts can be specified. The suggested tip amounts must be positive, passed in a strictly increased order and must not exceed max_tip_amount.
    :param protect_content:
    :return:
    """
    ...

def answer_shipping_query(token, shipping_query_id, ok, shipping_options=..., error_message=...):
    """
    If you sent an invoice requesting a shipping address and the parameter is_flexible was specified, the Bot API will send an Update with a shipping_query field to the bot. Use this method to reply to shipping queries. On success, True is returned.
    :param token: Bot's token (you don't need to fill this)
    :param shipping_query_id: Unique identifier for the query to be answered
    :param ok: Specify True if delivery to the specified address is possible and False if there are any problems (for example, if delivery to the specified address is not possible)
    :param shipping_options: Required if ok is True. A JSON-serialized array of available shipping options.
    :param error_message: Required if ok is False. Error message in human readable form that explains why it is impossible to complete the order (e.g. "Sorry, delivery to your desired address is unavailable'). Telegram will display this message to the user.
    :return:
    """
    ...

def answer_pre_checkout_query(token, pre_checkout_query_id, ok, error_message=...):
    """
    Once the user has confirmed their payment and shipping details, the Bot API sends the final confirmation in the form of an Update with the field pre_checkout_query. Use this method to respond to such pre-checkout queries. On success, True is returned. Note: The Bot API must receive an answer within 10 seconds after the pre-checkout query was sent.
    :param token: Bot's token (you don't need to fill this)
    :param pre_checkout_query_id: Unique identifier for the query to be answered
    :param ok: Specify True if everything is alright (goods are available, etc.) and the bot is ready to proceed with the order. Use False if there are any problems.
    :param error_message: Required if ok is False. Error message in human readable form that explains the reason for failure to proceed with the checkout (e.g. "Sorry, somebody just bought the last of our amazing black T-shirts while you were busy filling out your payment details. Please choose a different color or garment!"). Telegram will display this message to the user.
    :return:
    """
    ...

def answer_callback_query(token, callback_query_id, text=..., show_alert=..., url=..., cache_time=...):
    """
    Use this method to send answers to callback queries sent from inline keyboards. The answer will be displayed to the user as a notification at the top of the chat screen or as an alert. On success, True is returned.
    Alternatively, the user can be redirected to the specified Game URL. For this option to work, you must first create a game for your bot via BotFather and accept the terms. Otherwise, you may use links like telegram.me/your_bot?start=XXXX that open your bot with a parameter.
    :param token: Bot's token (you don't need to fill this)
    :param callback_query_id: Unique identifier for the query to be answered
    :param text: (Optional) Text of the notification. If not specified, nothing will be shown to the user, 0-200 characters
    :param show_alert: (Optional) If true, an alert will be shown by the client instead of a notification at the top of the chat screen. Defaults to false.
    :param url: (Optional) URL that will be opened by the user's client. If you have created a Game and accepted the conditions via @Botfather, specify the URL that opens your game – note that this will only work if the query comes from a callback_game button.
    Otherwise, you may use links like telegram.me/your_bot?start=XXXX that open your bot with a parameter.
    :param cache_time: (Optional) The maximum amount of time in seconds that the result of the callback query may be cached client-side. Telegram apps will support caching starting in version 3.14. Defaults to 0.
    :return:
    """
    ...

def answer_inline_query(token, inline_query_id, results, cache_time=..., is_personal=..., next_offset=..., switch_pm_text=..., switch_pm_parameter=...):
    ...

def get_sticker_set(token, name):
    ...

def upload_sticker_file(token, user_id, png_sticker):
    ...

def create_new_sticker_set(token, user_id, name, title, emojis, png_sticker, tgs_sticker, contains_masks=..., mask_position=..., webm_sticker=...):
    ...

def add_sticker_to_set(token, user_id, name, emojis, png_sticker, tgs_sticker, mask_position, webm_sticker):
    ...

def set_sticker_position_in_set(token, sticker, position):
    ...

def delete_sticker_from_set(token, sticker):
    ...

def answer_web_app_query(token, web_app_query_id, result: types.InlineQueryResultBase):
    ...

def create_invoice_link(token, title, description, payload, provider_token, currency, prices, max_tip_amount=..., suggested_tip_amounts=..., provider_data=..., photo_url=..., photo_size=..., photo_width=..., photo_height=..., need_name=..., need_phone_number=..., need_email=..., need_shipping_address=..., send_phone_number_to_provider=..., send_email_to_provider=..., is_flexible=...):
    ...

def send_poll(token, chat_id, question, options, is_anonymous=..., type=..., allows_multiple_answers=..., correct_option_id=..., explanation=..., explanation_parse_mode=..., open_period=..., close_date=..., is_closed=..., disable_notification=..., reply_to_message_id=..., allow_sending_without_reply=..., reply_markup=..., timeout=..., explanation_entities=..., protect_content=...):
    ...

def stop_poll(token, chat_id, message_id, reply_markup=...):
    ...

def convert_input_media(media): # -> tuple[None, None]:
    ...

def convert_input_media_array(array): # -> tuple[str, dict[Unknown, Unknown]]:
    ...

class ApiException(Exception):
    """
    This class represents a base Exception thrown when a call to the Telegram API fails.
    In addition to an informative message, it has a `function_name` and a `result` attribute, which respectively
    contain the name of the failed function and the returned result that made the function to be considered  as
    failed.
    """
    def __init__(self, msg, function_name, result) -> None:
        ...
    


class ApiHTTPException(ApiException):
    """
    This class represents an Exception thrown when a call to the 
    Telegram API server returns HTTP code that is not 200.
    """
    def __init__(self, function_name, result) -> None:
        ...
    


class ApiInvalidJSONException(ApiException):
    """
    This class represents an Exception thrown when a call to the 
    Telegram API server returns invalid json.
    """
    def __init__(self, function_name, result) -> None:
        ...
    


class ApiTelegramException(ApiException):
    """
    This class represents an Exception thrown when a Telegram API returns error code.
    """
    def __init__(self, function_name, result, result_json) -> None:
        ...
    


