from bot.config import EMOJI, CHANNEL_URL, SUPPORT_URL, ESCROW_URL


def ce(emoji_key: str) -> str:
    emoji_id = EMOJI.get(emoji_key, "")
    return f'<tg-emoji emoji-id="{emoji_id}">⭐</tg-emoji>'


TEXTS = {
    "ru": {
        "welcome": (
            f'{ce("wave")} Добро пожаловать\n\n'
            f'{ce("briefcase")} NotCoin P2P - Мы специализированный сервис по обеспечению безопасности вне биржевых сделок.\n\n'
            f'{ce("sparkles")} Автоматизированный алгоритм исполнения.\n'
            f'Скорость и автоматизация.\n'
            f'{ce("card")} Удобный и быстрый вывод средств.\n\n'
            f'• Комиссия сервиса: 1%\n'
            f'• Режим работы: 24/7\n'
            f'• Техническая поддержка: @NotCoinSafety\n\n'
            f'{ce("shield")} Выберите нужный раздел ниже:'
        ),
        "choose_role": (
            f'{ce("choose")} Выберите вашу роль'
        ),
        "choose_type": "Выберите тип товара для сделки:",
        "choose_payment": (
            f'{ce("briefcase")} Создание сделки\n\n'
            f'{ce("cart")} {{deal_type}}\n\n'
            f'Выберите метод получения оплаты:'
        ),
        "enter_amount": (
            f'{ce("briefcase")} Создание сделки\n\n'
            f'Введите сумму ({{currency}}) в формате: 100.5'
        ),
        "enter_description_nft_gift": (
            f'{ce("nft_gift_icon")} NFT-Подарок / Подарок:\n\n'
            f'Введите ссылку(-и) на подарок(-и) в одном из форматов:\n\n'
            f'https://... или t.me/...\n\n'
            f'Пример:\nt.me/nft/PlushPepe-1\n\n'
            f'Если у вас несколько подарков, указывайте каждую ссылку с новой строки.'
        ),
        "enter_description_channel": (
            f'{ce("channel")} Канал / Чат:\n\n'
            f'Введите ссылку на канал или чат:\n\n'
            f'Пример: https://t.me/yourchannel\n\n'
            f'Убедитесь что вы являетесь владельцем канала.'
        ),
        "enter_description_stars": (
            f'{ce("stars")} Звезды:\n\n'
            f'Введите количество звезд и username получателя:\n\n'
            f'Пример: 100 @username'
        ),
        "enter_description_username": (
            f'{ce("tag")} NFT-юзернеймы / Тег:\n\n'
            f'Введите username или ссылку на Fragment:\n\n'
            f'Пример: @coolname или https://fragment.com/username/coolname'
        ),
        "enter_description_other": (
            f'{ce("other")} Другое:\n\n'
            f'Опишите товар или услугу максимально подробно.\n\n'
            f'Покупатель увидит ваше описание перед оплатой.'
        ),
        "deal_created": (
            f'{ce("check")} Сделка успешно создана!\n\n'
            f'Сумма: {{amount}} {{currency_label}}\n'
            f'{ce("sparkles")} Валюта: {{currency_label}}\n'
            f'{ce("cart")} Товар: {{deal_type}}\n'
            f'{ce("scroll")} Описание: {{description}}\n'
            f'Ссылка для покупателя:\n'
            f'https://t.me/{{bot_username}}?start={{deal_id}}\n\n'
            f'Скопируйте ссылку и отправьте покупателю.'
        ),
        "deal_card_buyer": (
            f'{ce("card")} Информация о сделке #{{deal_id}}\n\n'
            f'{ce("wave")} Вы покупатель в сделке.\n'
            f'{ce("letter")} Продавец: @{{seller_username}}\n\n'
            f'{ce("scroll")} Вы покупаете: {{description}}\n\n'
            f'{ce("cart")} Товар: {{deal_type}}\n\n'
            f'{ce("briefcase")} Способ оплаты: {{payment_method}}\n\n'
            f'ID сделки: {{deal_id}}\n\n'
            f'Сумма к оплате: {{amount}} {{currency_label}}\n\n'
            f'Пожалуйста, следуйте инструкциям продавца по оплате.\n'
            f'Сохраните ID сделки для подтверждения!\n\n'
            f'В случае проблем с оплатой обратитесь в поддержку — {ESCROW_URL}'
        ),
        "payment_confirmed_buyer": (
            f'{ce("check")} Оплата подтверждена! Продавец уведомлен о вашем платеже.\n\n'
            f'{ce("cash")} Ожидайте подтверждения передачи товара от менеджера...\n\n'
            f'{ce("folder")} Ваша статистика будет обновлена после подтверждения менеджером.\n\n'
            f'Ожидайте получения товара через менеджера.'
        ),
        "user_joined_deal": (
            f'{ce("wave")} Пользователь @{{username}}\n'
            f'Присоединился к сделке #{{deal_id}}\n\n'
            f'{ce("folder")} Успешных сделок покупателя: {{deals_count}}\n'
            f'{ce("check")} Проверенный пользователь\n\n'
            f'Проверьте соответствие пользователя'
        ),
        "payment_notify_seller": (
            f'ПЛАТЁЖ ПОДТВЕРЖДЁН!\n\n'
            f'{ce("check")} Покупатель @{{buyer_username}} подтвердил оплату\n'
            f'{ce("scroll")} Сделка: #{{deal_id}}\n'
            f'{ce("briefcase")} Товар: {{description}}\n'
            f'{ce("cash")} Сумма: {{amount}} {{currency_label}}\n\n'
            f'{ce("folder")} Финансовые условия:\n'
            f'• Комиссия системы: 1% ({{commission}} {{currency_label}})\n'
            f'• К зачислению на баланс: {{amount_after}} {{currency_label}}\n\n'
            f'ТРЕБУЕТСЯ ВАШЕ ДЕЙСТВИЕ:\n'
            f'1. Передайте товар менеджеру {ESCROW_URL}\n'
            f'2. После передачи нажмите кнопку ниже\n'
            f'3. Менеджер подтвердит получение товара\n'
            f'4. Сумма {{amount_after}} {{currency_label}} будет зачислена на ваш баланс\n\n'
            f'{ce("cross")} Не передавайте товар покупателю напрямую!'
        ),
        "deal_completed_seller": (
            f'{ce("check")} Сделка успешно завершена!\n\n'
            f'{ce("cash")} Сумма {{amount_after}} {{currency_label}} зачислена на ваш баланс.\n\n'
            f'{ce("folder")} Статистика обновлена.\n'
            f'{ce("cart")} Сделка #{{deal_id}} закрыта.\n\n'
            f'Спасибо за использование Notcoin P2P!\n'
            f'{ce("channel")} Наш канал: @notcoin'
        ),
        "balance": (
            f'ВАШ БАЛАНС\n\n'
            f'{ce("wave")} Пользователь: @{{username}}\n\n'
            f'Доступные средства:\n'
            f'{ce("cash")} {{balance_rub}} RUB\n'
            f'{ce("coin")} {{balance_ton}} TON\n'
            f'{{balance_stars}} Stars\n\n'
            f'{ce("card")} Информация о выводе средств:\n'
            f'{ce("coin")} TON-кошелек: {{ton_status}}\n'
            f'{ce("card")} Карта / СБП: {{card_status}}\n\n'
            f'{ce("folder")} Информация:\n'
            f'• Комиссия системы: 1%\n'
            f'• Вывод доступен на карту, номер или TON-кошелек\n\n'
            f'{ce("briefcase")} Успешных сделок: {{deals_count}}'
        ),
        "withdraw_info": (
            f'{ce("cash")} Вывод средств\n\n'
            f'Ваша заявка на вывод принята.\n\n'
            f'⏳ Обработка занимает до 24 часов — каждая транзакция проходит многоуровневую проверку безопасности.\n\n'
            f'{ce("folder")} После проверки средства поступят на ваши реквизиты автоматически.\n\n'
            f'По вопросам: @NotCoinSafety'
        ),
        "operations_empty": (
            f'{ce("folder")} История операций\n\n'
            f'История пуста.'
        ),
        "operations_header": f'{ce("folder")} История операций\n\n',
        "requisites": (
            f'{ce("letter")} Управление реквизитами\n\n'
            f'{ce("coin")} TON-кошелек: {{ton_status}}\n'
            f'{ce("card")} Карта/телефон: {{card_status}}\n\n'
            f'Используйте кнопки ниже чтобы добавить/изменить реквизиты ✈️'
        ),
        "enter_ton_wallet": (
            f'{ce("coin")} Добавьте ваш TON-кошелек:\n\n'
            f'Пожалуйста, отправьте адрес вашего кошелька\n\n'
            f'Важно:\n'
            f'• Минимальная сумма вывода: 2.0 TON'
        ),
        "ton_wallet_saved": f'{ce("check")} TON-кошелек успешно сохранён!',
        "choose_card_region": (
            f'Выберите регион вашей карты / телефона:\n\n'
            f'Поддерживаются карты и номера\n'
            f'России, Казахстана, Украины и Беларуси.'
        ),
        "enter_card_number": (
            f'{ce("card")} Введите номер карты или телефона:\n\n'
            f'Пример: 4276 1234 5678 9012 или +79001234567'
        ),
        "card_saved": f'{ce("check")} Реквизиты успешно сохранены!',
        "referrals": (
            f'Реферальная программа\n\n'
            f'Приглашайте друзей и получайте бонусы!\n\n'
            f'Ваша реферальная ссылка:\n'
            f'https://t.me/{{bot_username}}?start=ref_{{referral_code}}\n\n'
            f'Статистика:\n'
            f'• Приглашено: {{invited_count}}\n'
            f'• Бонусов получено: {{bonus}} RUB\n\n'
            f'За каждого приглашённого друга вы получаете бонус на баланс!'
        ),
        "appeals": (
            'NotCoin P2P\nЦентр обращений\n\n'
            'Площадка для предложений и жалоб. Каждое обращение проверяется вручную.\n\n'
            '———\n\n'
            'Предложения\n'
            'Функционал и новые фичи\n'
            'Интеграции с биржами\n'
            'Отзывы о работе сервиса\n\n'
            'Жалобы\n'
            'Спорные транзакции\n'
            'Технические сбои\n'
            'Нарушения правил\n'
            'Подозрение на скам\n\n'
            '———\n\n'
            'Регламент\n\n'
            'Ответ в течение 24 часов\n'
            'Полная конфиденциальность\n'
            'Скам — мгновенная реакция\n'
            'Лучшие идеи внедряются\n\n'
            'Выберите тип обращения:'
        ),
        "appeals_stub": "Раздел в разработке. Скоро будет доступен!",
        "choose_language": "Выберите язык / Choose language / اختر اللغة:",
        "not_added": f'{ce("cross")} Не добавлен',
        "added": f'{ce("check")} Добавлен',
        "btn_create_deal": "Создать сделку",
        "btn_balance": "Мой баланс",
        "btn_requisites": "Реквизиты",
        "btn_channel": "Канал ↗",
        "btn_appeals": "Обращения",
        "btn_referrals": "Рефералы",
        "btn_support": "Поддержка ↗",
        "btn_mini_app": "Мини-приложение ↗",
        "btn_change_lang": "Изменить язык",
        "btn_back_menu": "Вернуться в меню",
        "btn_seller": "Я продавец",
        "btn_buyer": "Я покупатель",
        "btn_nft_gift": "NFT-Подарок / Подарок",
        "btn_channel_type": "Канал / Чат",
        "btn_stars": "Звезды",
        "btn_username": "NFT-юзернеймы / Тег",
        "btn_other": "Другое",
        "btn_cancel": "Отмена",
        "btn_ton_payment": "На TON-Кошелек",
        "btn_card_payment": "Перевод На карту / СБП",
        "btn_stars_payment": "Звезды",
        "btn_add_ton": "Добавить/Изменить TON-Кошелек",
        "btn_add_card": "Добавить карту / номер телефона",
        "btn_withdraw": "Вывести средства",
        "btn_operations": "История операций",
        "btn_suggest": "Предложить",
        "btn_complain": "Пожаловаться",
        "btn_back": "Назад",
        "btn_confirm_payment": "Подтвердить оплату",
        "btn_exit_deal": "Выйти со сделки",
        "btn_confirm_transfer": "Подтвердить передачу товара",
        "btn_cancel_deal": "Отменить сделку",
        "err_invalid_amount": "Введите корректную сумму, например: 100.5",
        "err_invalid_format": "Некорректный формат. Проверьте данные и попробуйте снова.",
        "err_deal_not_found": "Сделка не найдена.",
        "err_you_are_seller": "Вы являетесь продавцом этой сделки. Отправьте ссылку покупателю.",
        "err_deal_closed": "Эта сделка уже завершена или отменена.",
        "err_join_failed": "Не удалось присоединиться к сделке.",
        "err_not_buyer": "Вы не являетесь покупателем этой сделки.",
        "err_cant_confirm": "Невозможно подтвердить оплату для этой сделки.",
        "err_not_seller": "Вы не являетесь продавцом этой сделки.",
        "err_cant_complete": "Невозможно завершить сделку на данном этапе.",
        "err_invalid_wallet": "Некорректный адрес кошелька. Попробуйте снова.",
        "err_invalid_card": "Некорректные реквизиты. Попробуйте снова.",
        "transfer_waiting_buyer": f"{ce('shield')} Товар передан менеджеру!\n\nОжидаем подтверждения от покупателя. Как только покупатель подтвердит получение — средства будут зачислены на ваш баланс.",
        "transfer_notify_buyer": f"{ce('shield')} Продавец @{{seller_username}} передал товар по сделке #{{deal_id}}!\n\nСумма: {{amount}} {{currency_label}}\n\nПожалуйста, подтвердите получение товара, нажав кнопку ниже.",
        "deal_completed_buyer": f"{ce('shield')} Сделка #{{deal_id}} успешно завершена!\n\nСпасибо за использование Notcoin P2P!",
        "err_buyer_cant_create": "Покупатель не может создавать сделки. Попросите продавца создать сделку и прислать вам ссылку.",
        "btn_confirm_receive": "✅ Подтвердить получение товара",
        "deal_type_nft_gift": "NFT-Подарок / Подарок",
        "deal_type_channel": "Канал / Чат",
        "deal_type_stars": "Звезды",
        "deal_type_username": "NFT-юзернеймы / Тег",
        "deal_type_other": "Другое",
        "payment_ton": "На TON-Кошелек",
        "payment_card": "Перевод На карту / СБП",
        "payment_stars": "Звезды",

    },
    "en": {
        "welcome": (
            f'{ce("wave")} Welcome\n\n'
            f'{ce("briefcase")} NotCoin P2P - We are a specialized service for ensuring the security of OTC transactions.\n\n'
            f'{ce("sparkles")} Automated execution algorithm.\n'
            f'Speed and automation.\n'
            f'{ce("card")} Convenient and fast withdrawal of funds.\n\n'
            f'• Service commission: 1%\n'
            f'• Working mode: 24/7\n'
            f'• Technical support: @NotCoinSafety\n\n'
            f'{ce("shield")} Select a section below:'
        ),
        "choose_role": f'{ce("choose")} Choose your role',
        "choose_type": "Select the type of product for the deal:",
        "choose_payment": (
            f'{ce("briefcase")} Creating a deal\n\n'
            f'{ce("cart")} {{deal_type}}\n\n'
            f'Select payment method:'
        ),
        "enter_amount": f'{ce("briefcase")} Creating a deal\n\nEnter amount ({{currency}}) in format: 100.5',
        "enter_description_nft_gift": (
            f'{ce("nft_gift_icon")} NFT-Gift / Gift:\n\n'
            f'Enter the link(s) to the gift(s) in one of the formats:\n\n'
            f'https://... or t.me/...\n\n'
            f'Example:\nt.me/nft/PlushPepe-1\n\n'
            f'If you have multiple gifts, enter each link on a new line.'
        ),
        "enter_description_channel": (
            f'{ce("channel")} Channel / Chat:\n\n'
            f'Enter the link to the channel or chat:\n\n'
            f'Example: https://t.me/yourchannel'
        ),
        "enter_description_stars": (
            f'{ce("stars")} Stars:\n\n'
            f'Enter the number of stars and recipient username:\n\n'
            f'Example: 100 @username'
        ),
        "enter_description_username": (
            f'{ce("tag")} NFT-usernames / Tag:\n\n'
            f'Enter username or Fragment link:\n\n'
            f'Example: @coolname or https://fragment.com/username/coolname'
        ),
        "enter_description_other": (
            f'{ce("other")} Other:\n\n'
            f'Describe the product or service in as much detail as possible.'
        ),
        "deal_created": (
            f'{ce("check")} Deal successfully created!\n\n'
            f'Amount: {{amount}} {{currency_label}}\n'
            f'{ce("sparkles")} Currency: {{currency_label}}\n'
            f'{ce("cart")} Product: {{deal_type}}\n'
            f'{ce("scroll")} Description: {{description}}\n'
            f'Buyer link:\nhttps://t.me/{{bot_username}}?start={{deal_id}}\n\n'
            f'Copy the link and send it to the buyer.'
        ),
        "deal_card_buyer": (
            f'{ce("card")} Deal info #{{deal_id}}\n\n'
            f'{ce("wave")} You are the buyer.\n'
            f'{ce("letter")} Seller: @{{seller_username}}\n\n'
            f'{ce("scroll")} You are buying: {{description}}\n\n'
            f'{ce("cart")} Product: {{deal_type}}\n\n'
            f'{ce("briefcase")} Payment method: {{payment_method}}\n\n'
            f'Deal ID: {{deal_id}}\n\n'
            f'Amount to pay: {{amount}} {{currency_label}}\n\n'
            f'Please follow the seller\'s payment instructions.\n'
            f'Save the Deal ID for confirmation!\n\n'
            f'If you have payment issues, contact support — {ESCROW_URL}'
        ),
        "payment_confirmed_buyer": (
            f'{ce("check")} Payment confirmed! The seller has been notified.\n\n'
            f'{ce("cash")} Awaiting confirmation of item transfer from the manager...\n\n'
            f'{ce("folder")} Your statistics will be updated after manager confirmation.\n\n'
            f'Await receipt of the item through the manager.'
        ),
        "user_joined_deal": (
            f'{ce("wave")} User @{{username}}\n'
            f'Joined deal #{{deal_id}}\n\n'
            f'{ce("folder")} Buyer\'s successful deals: {{deals_count}}\n'
            f'{ce("check")} Verified user\n\n'
            f'Check user compliance'
        ),
        "payment_notify_seller": (
            f'PAYMENT CONFIRMED!\n\n'
            f'{ce("check")} Buyer @{{buyer_username}} confirmed payment\n'
            f'{ce("scroll")} Deal: #{{deal_id}}\n'
            f'{ce("briefcase")} Product: {{description}}\n'
            f'{ce("cash")} Amount: {{amount}} {{currency_label}}\n\n'
            f'{ce("folder")} Financial terms:\n'
            f'• System commission: 1% ({{commission}} {{currency_label}})\n'
            f'• To be credited: {{amount_after}} {{currency_label}}\n\n'
            f'ACTION REQUIRED:\n'
            f'1. Transfer the item to the manager {ESCROW_URL}\n'
            f'2. Click the button below after transfer\n'
            f'3. Manager will confirm receipt\n'
            f'4. {{amount_after}} {{currency_label}} will be credited to your balance\n\n'
            f'{ce("cross")} Do not transfer the item directly to the buyer!'
        ),
        "deal_completed_seller": (
            f'{ce("check")} Deal successfully completed!\n\n'
            f'{ce("cash")} {{amount_after}} {{currency_label}} credited to your balance.\n\n'
            f'{ce("folder")} Statistics updated.\n'
            f'{ce("cart")} Deal #{{deal_id}} closed.\n\n'
            f'Thank you for using Notcoin P2P!\n'
            f'{ce("channel")} Our channel: @notcoin'
        ),
        "balance": (
            f'YOUR BALANCE\n\n'
            f'{ce("wave")} User: @{{username}}\n\n'
            f'Available funds:\n'
            f'{ce("cash")} {{balance_rub}} RUB\n'
            f'{ce("coin")} {{balance_ton}} TON\n'
            f'{{balance_stars}} Stars\n\n'
            f'{ce("card")} Withdrawal info:\n'
            f'{ce("coin")} TON wallet: {{ton_status}}\n'
            f'{ce("card")} Card / SBP: {{card_status}}\n\n'
            f'{ce("folder")} Info:\n'
            f'• Commission: 1%\n'
            f'• Withdrawal available to card, phone or TON wallet\n\n'
            f'{ce("briefcase")} Successful deals: {{deals_count}}'
        ),
        "withdraw_info": (
            f'{ce("cash")} Withdrawal\n\n'
            f'Your withdrawal request has been accepted.\n\n'
            f'⏳ Processing takes up to 24 hours — each transaction undergoes multi-level security checks.\n\n'
            f'{ce("folder")} Funds will be sent to your requisites automatically.\n\n'
            f'Questions: @NotCoinSafety'
        ),
        "operations_empty": f'{ce("folder")} Operations history\n\nHistory is empty.',
        "operations_header": f'{ce("folder")} Operations history\n\n',
        "requisites": (
            f'{ce("letter")} Requisites management\n\n'
            f'{ce("coin")} TON wallet: {{ton_status}}\n'
            f'{ce("card")} Card/phone: {{card_status}}\n\n'
            f'Use the buttons below to add/change requisites ✈️'
        ),
        "enter_ton_wallet": (
            f'{ce("coin")} Add your TON wallet:\n\n'
            f'Please send your wallet address\n\n'
            f'Important:\n'
            f'• Minimum withdrawal: 2.0 TON'
        ),
        "ton_wallet_saved": f'{ce("check")} TON wallet successfully saved!',
        "choose_card_region": (
            f'Select your card / phone region:\n\n'
            f'Supported cards and numbers from\n'
            f'Russia, Kazakhstan, Ukraine and Belarus.'
        ),
        "enter_card_number": (
            f'{ce("card")} Enter card or phone number:\n\n'
            f'Example: 4276 1234 5678 9012 or +79001234567'
        ),
        "card_saved": f'{ce("check")} Requisites successfully saved!',
        "referrals": (
            f'Referral program\n\n'
            f'Invite friends and get bonuses!\n\n'
            f'Your referral link:\n'
            f'https://t.me/{{bot_username}}?start=ref_{{referral_code}}\n\n'
            f'Statistics:\n'
            f'• Invited: {{invited_count}}\n'
            f'• Bonuses received: {{bonus}} RUB\n\n'
            f'For each invited friend you get a balance bonus!'
        ),
        "appeals": (
            'NotCoin P2P\nAppeals Center\n\n'
            'Platform for suggestions and complaints. Each appeal is reviewed manually.\n\n'
            '———\n\n'
            'Suggestions\nFeatures and new functionality\nExchange integrations\nService reviews\n\n'
            'Complaints\nDisputed transactions\nTechnical issues\nRule violations\nScam suspicion\n\n'
            '———\n\n'
            'Regulations\n\nResponse within 24 hours\nFull confidentiality\nScam — instant reaction\nBest ideas implemented\n\n'
            'Select appeal type:'
        ),
        "appeals_stub": "Section under development. Coming soon!",
        "choose_language": "Выберите язык / Choose language / اختر اللغة:",
        "not_added": f'{ce("cross")} Not added',
        "added": f'{ce("check")} Added',
        "btn_create_deal": "Create deal",
        "btn_balance": "My balance",
        "btn_requisites": "Requisites",
        "btn_channel": "Channel ↗",
        "btn_appeals": "Appeals",
        "btn_referrals": "Referrals",
        "btn_support": "Support ↗",
        "btn_mini_app": "Mini-app ↗",
        "btn_change_lang": "Change language",
        "btn_back_menu": "Back to menu",
        "btn_seller": "I am Seller",
        "btn_buyer": "I am Buyer",
        "btn_nft_gift": "NFT-Gift / Gift",
        "btn_channel_type": "Channel / Chat",
        "btn_stars": "Stars",
        "btn_username": "NFT-usernames / Tag",
        "btn_other": "Other",
        "btn_cancel": "Cancel",
        "btn_ton_payment": "To TON Wallet",
        "btn_card_payment": "Card / SBP transfer",
        "btn_stars_payment": "Stars",
        "btn_add_ton": "Add/Change TON Wallet",
        "btn_add_card": "Add card / phone number",
        "btn_withdraw": "Withdraw funds",
        "btn_operations": "Operations history",
        "btn_suggest": "Suggest",
        "btn_complain": "Complain",
        "btn_back": "Back",
        "btn_confirm_payment": "Confirm payment",
        "btn_exit_deal": "Exit deal",
        "btn_confirm_transfer": "Confirm item transfer",
        "btn_cancel_deal": "Cancel deal",
        "err_invalid_amount": "Enter a valid amount, e.g.: 100.5",
        "err_invalid_format": "Invalid format. Please check your data and try again.",
        "err_deal_not_found": "Deal not found.",
        "err_you_are_seller": "You are the seller of this deal. Send the link to the buyer.",
        "err_deal_closed": "This deal is already completed or cancelled.",
        "err_join_failed": "Failed to join the deal.",
        "err_not_buyer": "You are not the buyer of this deal.",
        "err_cant_confirm": "Cannot confirm payment for this deal.",
        "err_not_seller": "You are not the seller of this deal.",
        "err_cant_complete": "Cannot complete the deal at this stage.",
        "err_invalid_wallet": "Invalid wallet address. Please try again.",
        "err_invalid_card": "Invalid requisites. Please try again.",
        "transfer_waiting_buyer": "✅ Item transferred to manager!\n\nWaiting for buyer confirmation. Once the buyer confirms receipt — funds will be credited to your balance.",
        "transfer_notify_buyer": "🛡 Seller @{seller_username} has transferred the item for deal #{deal_id}!\n\nAmount: {amount} {currency_label}\n\nPlease confirm receipt by pressing the button below.",
        "deal_completed_buyer": "🛡 Deal #{deal_id} successfully completed!\n\nThank you for using Notcoin P2P!",
        "err_buyer_cant_create": "Buyers cannot create deals. Ask the seller to create a deal and send you the link.",
        "btn_confirm_receive": "✅ Confirm receipt of item",
        "deal_type_nft_gift": "NFT-Gift / Gift",
        "deal_type_channel": "Channel / Chat",
        "deal_type_stars": "Stars",
        "deal_type_username": "NFT-usernames / Tag",
        "deal_type_other": "Other",
        "payment_ton": "To TON Wallet",
        "payment_card": "Card / SBP transfer",
        "payment_stars": "Stars",

    },
    "ar": {
        "welcome": (
            f'{ce("wave")} مرحباً بك\n\n'
            f'{ce("briefcase")} NotCoin P2P - نحن خدمة متخصصة لضمان أمان المعاملات خارج البورصة.\n\n'
            f'{ce("sparkles")} خوارزمية تنفيذ آلية.\n'
            f'السرعة والأتمتة.\n'
            f'{ce("card")} سحب سريع ومريح للأموال.\n\n'
            f'• عمولة الخدمة: 1%\n'
            f'• ساعات العمل: 24/7\n'
            f'• الدعم الفني: @NotCoinSafety\n\n'
            f'{ce("shield")} اختر القسم المطلوب أدناه:'
        ),
        "choose_role": f'{ce("choose")} اختر دورك',
        "choose_type": "اختر نوع المنتج للصفقة:",
        "choose_payment": f'{ce("briefcase")} إنشاء صفقة\n\n{ce("cart")} {{deal_type}}\n\nاختر طريقة الدفع:',
        "enter_amount": f'{ce("briefcase")} إنشاء صفقة\n\nأدخل المبلغ ({{currency}}) بالصيغة: 100.5',
        "enter_description_nft_gift": f'{ce("nft_gift_icon")} NFT-هدية:\n\nأدخل رابط الهدية:\n\nمثال: t.me/nft/PlushPepe-1',
        "enter_description_channel": f'{ce("channel")} القناة / المجموعة:\n\nأدخل رابط القناة:\n\nمثال: https://t.me/yourchannel',
        "enter_description_stars": f'{ce("stars")} النجوم:\n\nأدخل عدد النجوم واسم المستخدم:\n\nمثال: 100 @username',
        "enter_description_username": f'{ce("tag")} NFT-اسم المستخدم:\n\nأدخل اسم المستخدم أو رابط Fragment',
        "enter_description_other": f'{ce("other")} أخرى:\n\nصف المنتج أو الخدمة بالتفصيل.',
        "deal_created": (
            f'{ce("check")} تم إنشاء الصفقة بنجاح!\n\n'
            f'المبلغ: {{amount}} {{currency_label}}\n'
            f'{ce("sparkles")} العملة: {{currency_label}}\n'
            f'{ce("cart")} المنتج: {{deal_type}}\n'
            f'{ce("scroll")} الوصف: {{description}}\n'
            f'رابط المشتري:\nhttps://t.me/{{bot_username}}?start={{deal_id}}\n\n'
            f'انسخ الرابط وأرسله للمشتري.'
        ),
        "deal_card_buyer": (
            f'{ce("card")} معلومات الصفقة #{{deal_id}}\n\n'
            f'{ce("wave")} أنت المشتري.\n'
            f'{ce("letter")} البائع: @{{seller_username}}\n\n'
            f'{ce("scroll")} أنت تشتري: {{description}}\n\n'
            f'{ce("cart")} المنتج: {{deal_type}}\n\n'
            f'{ce("briefcase")} طريقة الدفع: {{payment_method}}\n\n'
            f'معرف الصفقة: {{deal_id}}\n\n'
            f'المبلغ المطلوب: {{amount}} {{currency_label}}\n\n'
            f'يرجى اتباع تعليمات البائع للدفع.\n'
            f'احفظ معرف الصفقة للتأكيد!\n\n'
            f'في حالة وجود مشاكل تواصل مع الدعم — {ESCROW_URL}'
        ),
        "payment_confirmed_buyer": f'{ce("check")} تم تأكيد الدفع!\n\n{ce("cash")} انتظر تأكيد نقل المنتج من المدير...\n\n{ce("folder")} ستُحدَّث إحصائياتك بعد تأكيد المدير.',
        "user_joined_deal": f'{ce("wave")} المستخدم @{{username}}\nانضم إلى الصفقة #{{deal_id}}\n\n{ce("folder")} صفقات المشتري الناجحة: {{deals_count}}\n{ce("check")} مستخدم موثق',
        "payment_notify_seller": f'تم تأكيد الدفع!\n\n{ce("check")} المشتري @{{buyer_username}} أكد الدفع\n{ce("scroll")} الصفقة: #{{deal_id}}\n{ce("briefcase")} المنتج: {{description}}\n{ce("cash")} المبلغ: {{amount}} {{currency_label}}\n\n{ce("folder")} الشروط المالية:\n• عمولة النظام: 1% ({{commission}} {{currency_label}})\n• للإضافة إلى الرصيد: {{amount_after}} {{currency_label}}\n\nمطلوب منك:\n1. أرسل المنتج للمدير {ESCROW_URL}\n2. اضغط الزر أدناه بعد الإرسال\n\n{ce("cross")} لا ترسل المنتج مباشرة للمشتري!',
        "deal_completed_seller": f'{ce("check")} اكتملت الصفقة بنجاح!\n\n{ce("cash")} تم إضافة {{amount_after}} {{currency_label}} إلى رصيدك.\n\n{ce("folder")} تم تحديث الإحصائيات.\n{ce("cart")} الصفقة #{{deal_id}} مغلقة.\n\nشكراً لاستخدام Notcoin P2P!\n{ce("channel")} قناتنا: @notcoin',
        "balance": f'رصيدك\n\n{ce("wave")} المستخدم: @{{username}}\n\nالأموال المتاحة:\n{ce("cash")} {{balance_rub}} RUB\n{ce("coin")} {{balance_ton}} TON\n{{balance_stars}} Stars\n\n{ce("card")} معلومات السحب:\n{ce("coin")} محفظة TON: {{ton_status}}\n{ce("card")} البطاقة / SBP: {{card_status}}\n\n{ce("folder")} معلومات:\n• العمولة: 1%\n\n{ce("briefcase")} الصفقات الناجحة: {{deals_count}}',
        "withdraw_info": f'{ce("cash")} سحب الأموال\n\nتم قبول طلب السحب.\n\n⏳ المعالجة تستغرق حتى 24 ساعة.\n\n{ce("folder")} ستُرسل الأموال تلقائياً.\n\nللاستفسار: @NotCoinSafety',
        "operations_empty": f'{ce("folder")} سجل العمليات\n\nالسجل فارغ.',
        "operations_header": f'{ce("folder")} سجل العمليات\n\n',
        "requisites": f'{ce("letter")} إدارة التفاصيل البنكية\n\n{ce("coin")} محفظة TON: {{ton_status}}\n{ce("card")} البطاقة/الهاتف: {{card_status}}\n\nاستخدم الأزرار أدناه للإضافة/التعديل ✈️',
        "enter_ton_wallet": f'{ce("coin")} أضف محفظة TON:\n\nأرسل عنوان محفظتك\n\nمهم:\n• الحد الأدنى للسحب: 2.0 TON',
        "ton_wallet_saved": f'{ce("check")} تم حفظ محفظة TON بنجاح!',
        "choose_card_region": 'اختر منطقة بطاقتك / هاتفك:',
        "enter_card_number": f'{ce("card")} أدخل رقم البطاقة أو الهاتف:',
        "card_saved": f'{ce("check")} تم حفظ التفاصيل بنجاح!',
        "referrals": f'برنامج الإحالة\n\nادعُ أصدقاءك واحصل على مكافآت!\n\nرابط الإحالة:\nhttps://t.me/{{bot_username}}?start=ref_{{referral_code}}\n\nالإحصائيات:\n• المدعوون: {{invited_count}}\n• المكافآت: {{bonus}} RUB',
        "appeals": 'NotCoin P2P\nمركز الاستفسارات\n\nمنصة للمقترحات والشكاوى.\n\nاختر نوع الاستفسار:',
        "appeals_stub": "القسم قيد التطوير. قريباً!",
        "choose_language": "Выберите язык / Choose language / اختر اللغة:",
        "not_added": f'{ce("cross")} غير مضاف',
        "added": f'{ce("check")} مضاف',
        "btn_create_deal": "إنشاء صفقة",
        "btn_balance": "رصيدي",
        "btn_requisites": "التفاصيل البنكية",
        "btn_channel": "القناة ↗",
        "btn_appeals": "الاستفسارات",
        "btn_referrals": "الإحالات",
        "btn_support": "الدعم ↗",
        "btn_mini_app": "التطبيق المصغر ↗",
        "btn_change_lang": "تغيير اللغة",
        "btn_back_menu": "العودة للقائمة",
        "btn_seller": "أنا البائع",
        "btn_buyer": "أنا المشتري",
        "btn_nft_gift": "NFT-هدية / هدية",
        "btn_channel_type": "قناة / مجموعة",
        "btn_stars": "نجوم",
        "btn_username": "NFT-اسم مستخدم",
        "btn_other": "أخرى",
        "btn_cancel": "إلغاء",
        "btn_ton_payment": "إلى محفظة TON",
        "btn_card_payment": "تحويل بطاقة / SBP",
        "btn_stars_payment": "نجوم",
        "btn_add_ton": "إضافة/تعديل محفظة TON",
        "btn_add_card": "إضافة بطاقة / هاتف",
        "btn_withdraw": "سحب الأموال",
        "btn_operations": "سجل العمليات",
        "btn_suggest": "اقتراح",
        "btn_complain": "شكوى",
        "btn_back": "رجوع",
        "btn_confirm_payment": "تأكيد الدفع",
        "btn_exit_deal": "الخروج من الصفقة",
        "btn_confirm_transfer": "تأكيد نقل المنتج",
        "btn_cancel_deal": "إلغاء الصفقة",
        "err_invalid_amount": "أدخل مبلغاً صحيحاً، مثال: 100.5",
        "err_invalid_format": "صيغة غير صحيحة. تحقق من البيانات وحاول مجدداً.",
        "err_deal_not_found": "الصفقة غير موجودة.",
        "err_you_are_seller": "أنت بائع هذه الصفقة. أرسل الرابط للمشتري.",
        "err_deal_closed": "هذه الصفقة مكتملة أو ملغاة بالفعل.",
        "err_join_failed": "فشل الانضمام إلى الصفقة.",
        "err_not_buyer": "أنت لست مشتري هذه الصفقة.",
        "err_cant_confirm": "لا يمكن تأكيد الدفع لهذه الصفقة.",
        "err_not_seller": "أنت لست بائع هذه الصفقة.",
        "err_cant_complete": "لا يمكن إتمام الصفقة في هذه المرحلة.",
        "err_invalid_wallet": "عنوان المحفظة غير صحيح. حاول مجدداً.",
        "err_invalid_card": "بيانات غير صحيحة. حاول مجدداً.",
        "transfer_waiting_buyer": "✅ تم تسليم المنتج للمدير!\n\nبانتظار تأكيد المشتري. بمجرد تأكيد الاستلام — سيتم إضافة الأموال إلى رصيدك.",
        "transfer_notify_buyer": "🛡 البائع @{seller_username} سلّم المنتج للصفقة #{deal_id}!\n\nالمبلغ: {amount} {currency_label}\n\nيرجى تأكيد الاستلام بالضغط على الزر أدناه.",
        "deal_completed_buyer": "🛡 اكتملت الصفقة #{deal_id} بنجاح!\n\nشكراً لاستخدام Notcoin P2P!",
        "err_buyer_cant_create": "لا يمكن للمشتري إنشاء صفقات. اطلب من البائع إنشاء الصفقة وإرسال الرابط إليك.",
        "btn_confirm_receive": "✅ تأكيد استلام المنتج",
        "deal_type_nft_gift": "NFT-هدية / هدية",
        "deal_type_channel": "قناة / مجموعة",
        "deal_type_stars": "نجوم",
        "deal_type_username": "NFT-اسم مستخدم / تاغ",
        "deal_type_other": "أخرى",
        "payment_ton": "إلى محفظة TON",
        "payment_card": "تحويل بطاقة / SBP",
        "payment_stars": "نجوم",

    },
    "zh": {
        "welcome": (
            f'{ce("wave")} 欢迎\n\n'
            f'{ce("briefcase")} NotCoin P2P - 我们是专业的场外交易安全保障服务。\n\n'
            f'{ce("sparkles")} 自动化执行算法。\n'
            f'速度与自动化。\n'
            f'{ce("card")} 便捷快速提款。\n\n'
            f'• 服务佣金: 1%\n'
            f'• 工作模式: 24/7\n'
            f'• 技术支持: @NotCoinSafety\n\n'
            f'{ce("shield")} 请选择以下功能:'
        ),
        "choose_role": f'{ce("choose")} 选择您的角色',
        "choose_type": "选择交易商品类型:",
        "choose_payment": f'{ce("briefcase")} 创建交易\n\n{ce("cart")} {{deal_type}}\n\n选择付款方式:',
        "enter_amount": f'{ce("briefcase")} 创建交易\n\n请输入金额 ({{currency}})，格式: 100.5',
        "enter_description_nft_gift": f'{ce("nft_gift_icon")} NFT礼品:\n\n请输入礼品链接:\n\n示例: t.me/nft/PlushPepe-1',
        "enter_description_channel": f'{ce("channel")} 频道/群组:\n\n请输入频道链接:\n\n示例: https://t.me/yourchannel',
        "enter_description_stars": f'{ce("stars")} 星星:\n\n请输入星星数量和收款人用户名:\n\n示例: 100 @username',
        "enter_description_username": f'{ce("tag")} NFT用户名:\n\n请输入用户名或Fragment链接',
        "enter_description_other": f'{ce("other")} 其他:\n\n请详细描述商品或服务。',
        "deal_created": (
            f'{ce("check")} 交易创建成功!\n\n'
            f'金额: {{amount}} {{currency_label}}\n'
            f'{ce("sparkles")} 货币: {{currency_label}}\n'
            f'{ce("cart")} 商品: {{deal_type}}\n'
            f'{ce("scroll")} 描述: {{description}}\n'
            f'买家链接:\nhttps://t.me/{{bot_username}}?start={{deal_id}}\n\n'
            f'复制链接并发送给买家。'
        ),
        "deal_card_buyer": (
            f'{ce("card")} 交易信息 #{{deal_id}}\n\n'
            f'{ce("wave")} 您是买家。\n'
            f'{ce("letter")} 卖家: @{{seller_username}}\n\n'
            f'{ce("scroll")} 您购买: {{description}}\n\n'
            f'{ce("cart")} 商品: {{deal_type}}\n\n'
            f'{ce("briefcase")} 付款方式: {{payment_method}}\n\n'
            f'交易ID: {{deal_id}}\n\n'
            f'应付金额: {{amount}} {{currency_label}}\n\n'
            f'请按照卖家的付款说明操作。\n'
            f'请保存交易ID以供确认!\n\n'
            f'如有付款问题请联系客服 — {ESCROW_URL}'
        ),
        "payment_confirmed_buyer": f'{ce("check")} 付款已确认! 已通知卖家。\n\n{ce("cash")} 等待管理员确认商品转移...\n\n{ce("folder")} 管理员确认后将更新您的统计数据。',
        "user_joined_deal": f'{ce("wave")} 用户 @{{username}}\n已加入交易 #{{deal_id}}\n\n{ce("folder")} 买家成功交易数: {{deals_count}}\n{ce("check")} 已验证用户',
        "payment_notify_seller": f'付款已确认!\n\n{ce("check")} 买家 @{{buyer_username}} 确认付款\n{ce("scroll")} 交易: #{{deal_id}}\n{ce("briefcase")} 商品: {{description}}\n{ce("cash")} 金额: {{amount}} {{currency_label}}\n\n{ce("folder")} 财务条款:\n• 系统佣金: 1% ({{commission}} {{currency_label}})\n• 到账金额: {{amount_after}} {{currency_label}}\n\n需要您的操作:\n1. 将商品转交给管理员 {ESCROW_URL}\n2. 转交后点击下方按钮\n\n{ce("cross")} 请勿直接将商品转给买家!',
        "deal_completed_seller": f'{ce("check")} 交易成功完成!\n\n{ce("cash")} {{amount_after}} {{currency_label}} 已入账。\n\n{ce("folder")} 统计数据已更新。\n{ce("cart")} 交易 #{{deal_id}} 已关闭。\n\n感谢使用 Notcoin P2P!\n{ce("channel")} 我们的频道: @notcoin',
        "balance": f'您的余额\n\n{ce("wave")} 用户: @{{username}}\n\n可用资金:\n{ce("cash")} {{balance_rub}} RUB\n{ce("coin")} {{balance_ton}} TON\n{{balance_stars}} 星星\n\n{ce("card")} 提款信息:\n{ce("coin")} TON钱包: {{ton_status}}\n{ce("card")} 银行卡/电话: {{card_status}}\n\n{ce("folder")} 信息:\n• 佣金: 1%\n\n{ce("briefcase")} 成功交易数: {{deals_count}}',
        "withdraw_info": f'{ce("cash")} 提款\n\n您的提款申请已受理。\n\n⏳ 处理时间最长24小时。\n\n{ce("folder")} 资金将自动发送到您的账户。\n\n如有问题: @NotCoinSafety',
        "operations_empty": f'{ce("folder")} 操作历史\n\n历史为空。',
        "operations_header": f'{ce("folder")} 操作历史\n\n',
        "requisites": f'{ce("letter")} 收款信息管理\n\n{ce("coin")} TON钱包: {{ton_status}}\n{ce("card")} 银行卡/电话: {{card_status}}\n\n使用下方按钮添加/修改收款信息 ✈️',
        "enter_ton_wallet": f'{ce("coin")} 添加您的TON钱包:\n\n请发送钱包地址\n\n重要:\n• 最低提款: 2.0 TON',
        "ton_wallet_saved": f'{ce("check")} TON钱包保存成功!',
        "choose_card_region": '选择您的银行卡/电话区域:',
        "enter_card_number": f'{ce("card")} 请输入银行卡号或电话号码:',
        "card_saved": f'{ce("check")} 收款信息保存成功!',
        "referrals": f'推荐计划\n\n邀请朋友并获得奖励!\n\n您的推荐链接:\nhttps://t.me/{{bot_username}}?start=ref_{{referral_code}}\n\n统计:\n• 已邀请: {{invited_count}}\n• 获得奖励: {{bonus}} RUB',
        "appeals": 'NotCoin P2P\n申诉中心\n\n建议和投诉平台。\n\n选择申诉类型:',
        "appeals_stub": "该功能正在开发中。敬请期待!",
        "choose_language": "Выберите язык / Choose language / اختر اللغة:",
        "not_added": f'{ce("cross")} 未添加',
        "added": f'{ce("check")} 已添加',
        "btn_create_deal": "创建交易",
        "btn_balance": "我的余额",
        "btn_requisites": "收款信息",
        "btn_channel": "频道 ↗",
        "btn_appeals": "申诉",
        "btn_referrals": "推荐",
        "btn_support": "客服 ↗",
        "btn_mini_app": "小程序 ↗",
        "btn_change_lang": "更改语言",
        "btn_back_menu": "返回菜单",
        "btn_seller": "我是卖家",
        "btn_buyer": "我是买家",
        "btn_nft_gift": "NFT礼品 / 礼品",
        "btn_channel_type": "频道 / 群组",
        "btn_stars": "星星",
        "btn_username": "NFT用户名",
        "btn_other": "其他",
        "btn_cancel": "取消",
        "btn_ton_payment": "到TON钱包",
        "btn_card_payment": "银行卡转账",
        "btn_stars_payment": "星星",
        "btn_add_ton": "添加/修改TON钱包",
        "btn_add_card": "添加银行卡/电话",
        "btn_withdraw": "提款",
        "btn_operations": "操作历史",
        "btn_suggest": "建议",
        "btn_complain": "投诉",
        "btn_back": "返回",
        "btn_confirm_payment": "确认付款",
        "btn_exit_deal": "退出交易",
        "btn_confirm_transfer": "确认商品转移",
        "btn_cancel_deal": "取消交易",
        "err_invalid_amount": "请输入有效金额，例如: 100.5",
        "err_invalid_format": "格式无效。请检查数据后重试。",
        "err_deal_not_found": "未找到交易。",
        "err_you_are_seller": "您是此交易的卖家。请将链接发送给买家。",
        "err_deal_closed": "此交易已完成或已取消。",
        "err_join_failed": "加入交易失败。",
        "err_not_buyer": "您不是此交易的买家。",
        "err_cant_confirm": "无法确认此交易的付款。",
        "err_not_seller": "您不是此交易的卖家。",
        "err_cant_complete": "此阶段无法完成交易。",
        "err_invalid_wallet": "钱包地址无效，请重试。",
        "err_invalid_card": "收款信息无效，请重试。",
        "transfer_waiting_buyer": "✅ 商品已移交给管理员！\n\n等待买家确认。买家确认收货后 — 资金将记入您的余额。",
        "transfer_notify_buyer": "🛡 卖家 @{seller_username} 已为交易 #{deal_id} 移交商品！\n\n金额: {amount} {currency_label}\n\n请点击下方按钮确认收货。",
        "deal_completed_buyer": "🛡 交易 #{deal_id} 成功完成！\n\n感谢使用 Notcoin P2P！",
        "err_buyer_cant_create": "买家无法创建交易。请让卖家创建交易并将链接发送给您。",
        "btn_confirm_receive": "✅ 确认收到商品",
        "deal_type_nft_gift": "NFT礼品 / 礼品",
        "deal_type_channel": "频道 / 群组",
        "deal_type_stars": "星星",
        "deal_type_username": "NFT用户名 / 标签",
        "deal_type_other": "其他",
        "payment_ton": "到TON钱包",
        "payment_card": "银行卡转账 / SBP",
        "payment_stars": "星星",

    },
}


def get_text(lang: str, key: str, **kwargs) -> str:
    lang_texts = TEXTS.get(lang, TEXTS["ru"])
    text = lang_texts.get(key, TEXTS["ru"].get(key, ""))
    if kwargs:
        text = text.format(**kwargs)
    return text

def get_deal_type_label(lang: str, deal_type: str) -> str:
    key = f"deal_type_{deal_type}"
    return get_text(lang, key) or deal_type

def get_payment_label(lang: str, payment: str) -> str:
    key = f"payment_{payment}"
    return get_text(lang, key) or payment

