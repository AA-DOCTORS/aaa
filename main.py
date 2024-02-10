
# This is a sample Python script.
import telebot

TOKEN = '6576446964:AAGv2nfbnzEPZeDK0lOsPygsXH4mUjszcaI'
ADMIN_ID = '-988392444'

bot = telebot.TeleBot('6425975649:AAH_l1FAR3UNGQslOHLivFGUiOknwGq0exM')

name = None
username = None
user1_mess = None
user2_mess = None
user3_mess = None


@bot.message_handler(commands=['start'])
def start_message(message):
    global name, username
    name = message.from_user.first_name
    username = message.from_user.username
    bot.send_message(message.chat.id, "Привет! Это бот для заявок. Чтобы подать заявку, ответьте на вопросы.")
    form1(message)
def form1(message):
    global user1_mess
    user1_mess = message.text
    bot.send_message(message.chat.id, "ФИО:")
    bot.register_next_step_handler(message, form2)


def form2(message):
    global user2_mess
    user2_mess = message.text
    bot.send_message(message.chat.id, "Дата рождения:")
    bot.register_next_step_handler(message, form3)


def form3(message):
    global user3_mess
    user3_mess = message.text
    bot.send_message(message.chat.id, "Пол:")
    bot.register_next_step_handler(message, form4)


def form4(message):
    global user4_mess
    user4_mess = message.text
    bot.send_message(message.chat.id, "Контактный номер телефона:")
    bot.register_next_step_handler(message, form5)


def form5(message):
    global user5_mess
    user5_mess = message.text
    bot.send_message(message.chat.id, "Адрес проживания:")
    bot.register_next_step_handler(message, form6)


def form6(message):
    global user6_mess
    user6_mess = message.text
    bot.send_message(message.chat.id, "Когда вы в последний раз посещали стоматолога?")
    bot.register_next_step_handler(message, form7)


def form7(message):
    global user7_mess
    user7_mess = message.text
    bot.send_message(message.chat.id, "Были ли у вас ранее стоматологические операции или лечение?")
    bot.register_next_step_handler(message, form8)
    name = message.from_user.first_name


def form8(message):
    global user8_mess
    user8_mess = message.text
    bot.send_message(message.chat.id, " Есть ли у вас зубные капканы или мосты?")
    bot.register_next_step_handler(message, form9)


def form9(message):
    global user9_mess
    user9_mess = message.text
    bot.send_message(message.chat.id, "Имеете ли вы протезы?")
    bot.register_next_step_handler(message, form10)


def form10(message):
    global user10_mess
    user10_mess = message.text
    bot.send_message(message.chat.id, "Как вы оцениваете свою зубную гигиену?")
    bot.register_next_step_handler(message, form11)


def form11(message):
    global user11_mess
    user11_mess = message.text
    bot.send_message(message.chat.id, " Есть ли у вас боли в зубах или деснах? Где и какова интенсивность?")
    bot.register_next_step_handler(message, form12)


def form12(message):
    global user12_mess
    user12_mess = message.text
    bot.send_message(message.chat.id, "Замечаете ли вы кровоточивость десен при чистке зубов?")
    bot.register_next_step_handler(message, form13)


def form13(message):
    global user13_mess
    user13_mess = message.text
    bot.send_message(message.chat.id, " Есть ли у вас чувствительность зубов к холоду, горячему, сладкому или кислому?")
    bot.register_next_step_handler(message, form14)


def form14(message):
    global user14_mess
    user14_mess = message.text
    bot.send_message(message.chat.id, "Обнаружили ли вы что-то необычное в полости рта?")
    bot.register_next_step_handler(message, form15)


def form15(message):
    global user15_mess
    user15_mess = message.text
    bot.send_message(message.chat.id, "Замечали ли вы щелчки при открывании рта?")
    bot.register_next_step_handler(message, form16)


def form16(message):
    global user16_mess
    user16_mess = message.text
    bot.send_message(message.chat.id, "Имеются ли ограничения открывания рта?")
    bot.register_next_step_handler(message, form17)


def form17(message):
    global user17_mess
    user17_mess = message.text
    bot.send_message(message.chat.id, "Имеются ли у вас боли в области челюстей, ушей или головы?")
    bot.register_next_step_handler(message, form18)


def form18(message):
    global user18_mess
    user18_mess = message.text
    bot.send_message(message.chat.id, " Стискиваете ли вы зубы, особенно во сне?")
    bot.register_next_step_handler(message, form19)


def form19(message):
    global user19_mess
    user19_mess = message.text
    bot.send_message(message.chat.id, "Курите ли вы? Если да, сколько сигарет в день?")
    bot.register_next_step_handler(message, form20)


def form20(message):
    global user20_mess
    user20_mess = message.text
    bot.send_message(message.chat.id, " Пьете ли вы алкоголь? С какой периодичностью?")
    bot.register_next_step_handler(message, form21)


def form21(message):
    global user21_mess
    user21_mess = message.text
    bot.send_message(message.chat.id, "Как часто вы посещаете стоматолога для профессиональной гигиены полости рта?")
    bot.register_next_step_handler(message, form22)


def form22(message):
    global user22_mess
    user22_mess = message.text
    bot.send_message(message.chat.id, "Используете ли вы зубную нить или другие средства для чистки между зубами?")
    bot.register_next_step_handler(message, form23)


def form23(message):
    global user23_mess
    user23_mess = message.text
    bot.send_message(message.chat.id, "Есть ли у вас аллергии на лекарства или материалы, используемые в стоматологии?")
    bot.register_next_step_handler(message, form24)


def form24(message):
    global user24_mess
    user24_mess = message.text
    bot.send_message(message.chat.id, "Принимаете ли вы какие-либо медикаменты в настоящее время?")
    bot.register_next_step_handler(message, form25)


def form25(message):
    global user25_mess
    user25_mess = message.text
    bot.send_message(message.chat.id,
                     "  Есть ли у вас какие-либо медицинские проблемы, о которых стоматологу следует знать?")
    bot.register_next_step_handler(message, form26)


def form26(message):
    global user26_mess
    user26_mess = message.text
    bot.send_message(message.chat.id, "Есть ли у вас какие-либо конкретные ожидания от посещения стоматолога?")
    bot.register_next_step_handler(message, form27)

def form27(message):
        global user27_mess
        user27_mess = message.text
        bot.send_message(message.chat.id, "Спасибо вам за ваш труд! Напишите что угодно для того что бы отправить ваши ответы.")
        bot.register_next_step_handler(message, result)


def result(message):
    bot.send_message(message.chat.id, "Спасибо за заявку! Скоро наш менеджер свяжется с вами. Всего доброго!")
    admin_app(ADMIN_ID)


def admin_app(ADMIN_ID):
    ankets = f'''Новая заявка от {name}!
1. Личная Информация:
 • ФИО: {user2_mess}
 • Дата рождения: {user3_mess}
 • Пол: {user4_mess}
 • Контактный номер телефона: {user5_mess}
 • Адрес проживания: {user6_mess}
2. Зубная История:
 •   Когда вы последний раз посещали стоматолога? {user7_mess}
 •   Были ли у вас ранее стоматологические операции или лечение? {user8_mess}
 •   Есть ли у вас зубные капканы или мосты? {user9_mess}
 •   Имеете ли вы протезы? {user10_mess}
 •   Как вы оцениваете свою зубную гигиену? {user11_mess}
3. Жалобы:
 •   Есть ли у вас боли в зубах или деснах? Где и какова интенсивность? {user12_mess}
 •   Замечаете ли вы кровоточивость десен при чистке зубов? {user13_mess}
 •   Есть ли у вас чувствительность зубов к холоду, горячему, сладкому или кислому? {user14_mess}
 •   Обнаружили ли вы что-то необычное в полости рта? {user15_mess}
4. Симптомы Челюстно-Лицевой Системы:
 •   Замечали ли вы щелчки при открывании рта? {user16_mess}
 • Имеются ли ограничения открывания рта? {user17_mess}
 •   Имеются ли у вас боли в области челюстей, ушей или головы? {user18_mess}
 •   Стискиваете ли вы зубы, особенно во сне? {user19_mess}
5. Привычки и Образ Жизни:
 •   Курите ли вы? Если да, сколько сигарет в день? {user20_mess}
 •   Пьете ли вы алкоголь? С какой периодичностью? {user21_mess}
 •   Как часто вы посещаете стоматолога для профессиональной гигиены полости рта? {user22_mess}
 •   Используете ли вы зубную нить или другие средства для чистки между зубами? {user23_mess}
6. Прочие вопросы:
 •   Есть ли у вас аллергии на лекарства или материалы, используемые в стоматологии? {user24_mess}
 •   Принимаете ли вы какие-либо медикаменты в настоящее время? {user25_mess}
 •   Есть ли у вас какие-либо медицинские проблемы, о которых стоматологу следует знать? {user26_mess}
7. Пожелания и Ожидания:
 • Есть ли у вас какие-либо конкретные ожидания от посещения стоматолога? {user27_mess}

Telegram:
Name: {name}
Username: @{username}'''

    bot.send_message(ADMIN_ID, ankets)


bot.polling(none_stop=True)