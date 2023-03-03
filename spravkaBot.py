import telebot
from telebot import types
#TOKEN = '5619567760:AAE7Yc2-Q2ngDuU0B68Gxt4KpjDjGB5aTog' # bot token for real Bot

TOKEN = '5984037791:AAGJacq-SfwcklPBWUNSEgguGxZuRby12qY' # bot token for testing

bot = telebot.TeleBot(TOKEN)

def after_term():
    bot.send_message("Для начала работы со мной нажмите сюда - '/help'.")

def ID_list (zz):
    new_list = []
    with open('tumbd.txt','r+') as f:
        s = f.readlines()
        for x in s:
            x_res = int(x[:12])
            new_list.append(x_res)
    if zz not in new_list:
        new_list.append(zz)
    print(len(new_list))
    delim = '\n'
    ww = delim.join(map(str,new_list))
    with open('tumbd.txt','w') as f:
        f.write(ww)

# new_list =[]
# with open('tumbd.txt', 'r') as f_rass:
#     rass_list = f_rass.readlines()
#     for rass in rass_list:
#         x_rass = int(rass[:12])
#         bot.send_message(text='Обновление. Антибиотики +Бактопенем. Парентеральное питание кратко.\n'
#                               'Напишите, пожалуйста, что бы вы хотели ещё в этом боте.', chat_id=x_rass)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.reply_to(message, "Привет, я бот-справочник. У меня есть много разной полезной информации для врачей-реаниматологов. "
                          "Шучу, пока не очень много. Информация представлена в форме ветвящегося дерева - Вам достаточно просто "
                          "выбирать нужную кнопку.")
    bot.reply_to(message, "Слева есть меню, которое Вам подскажет, если что непонятно.")
    bot.reply_to(message, "Для начала работы со мной нажмите сюда - '/help'.")
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    ID_list(user_id)

@bot.message_handler(commands=['connect'])
def welcome(message):
    bot.reply_to(message, "Здравствуйте, меня зовут Алексей Мухин, "
                          "Если у вас возникли вопросы по работе бота или содержимому справочника (исправить или "
                          "предложить что добавить ещё и куда - то напишите мне на электронную почту с "
                          "соответствующей пометкой. Буду рад услышать конструктивные предложения. "
                          "kijiassa@gmail.com")

@bot.message_handler(commands=['pravo'])
def welcome(message):
    bot.reply_to(message, "Информация изложенная в данном боте-справочнике хоть и основана на официальных протоколах, инструкциях, "
                          "литературных источниках, но носит исключительно рекомендательный характер и не обязательна к "
                          "исполнению. Обязательно проверьте используемые данные, если есть хоть малейшие сомнения. Я, как "
                          "все остальные, могу ошибаться. А ответственность всегда лежит на враче.")


@bot.message_handler(commands=['help'])

def tree_start_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #включает клавиатуру, параметр - адаптирует размер кнопки
    butt1 = types.KeyboardButton('Лекарства') #собственно, кнопки
    butt2 = types.KeyboardButton('Лаборатория')
    butt3 = types.KeyboardButton('Патологии')
    butt4 = types.KeyboardButton('Быстрый доступ')
    markup.add(butt1, butt2, butt3, butt4) #объявление кнопок
    bot.send_message(message.chat.id, 'Чем могу помочь, <b>{0.first_name}?</b>'.format(message.from_user), reply_markup=markup, parse_mode='html')
                    # включение кнопок в ответ на сообщение юзера с личным обращением first name

@bot.message_handler(content_types=['text'])

def bot_message(message):
    if message.chat.type == 'private':
        if message.text == 'Лекарства':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Антибиотики')
            item2 = types.KeyboardButton('Миорелаксанты')
            item3 = types.KeyboardButton('Анальгоседация')
            item4 = types.KeyboardButton('Противогрибковые/вирусные')
            butback = types.KeyboardButton('В начало')
            markup.add(item1, item2, item3, item4, butback)
            bot.send_message(message.chat.id, 'Выберите группу препаратов'.format(message.from_user),reply_markup=markup)
        elif message.text == 'Лаборатория':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            butt1 = types.KeyboardButton('Общий анализ крови')
            butt2 = types.KeyboardButton('Биохимия (в работе)')
            butt3 = types.KeyboardButton('Анализ ликвора')
            butt4 = types.KeyboardButton('Анализ мочи (в работе)')
            butback = types.KeyboardButton('В начало')
            markup.add(butt1, butt2, butt3, butt4, butback)
            bot.send_message(message.chat.id, 'Выберите группу анализов'.format(message.from_user),reply_markup=markup)
        elif message.text == 'Патологии':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            butt1 = types.KeyboardButton('БЛД')
            butt2 = types.KeyboardButton('Метаболические нарушения')
            butt3 = types.KeyboardButton('Гипотермия')
            butt4 = types.KeyboardButton('ГБН. Желтуха')
            butt5 = types.KeyboardButton('Парентеральное питание')
            butback = types.KeyboardButton('В начало')
            markup.add(butt1, butt2, butt3, butt4, butt5, butback)
            bot.send_message(message.chat.id, 'Выберите патологию'.format(message.from_user),reply_markup=markup)

        elif message.text == 'Антибиотики':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            butt1 = types.KeyboardButton('Амикацин')
            butt2 = types.KeyboardButton('Гентамицин')
            butt3 = types.KeyboardButton('Ампициллин+сульбактам')
            butt4 = types.KeyboardButton('Тазоцин')
            butt5 = types.KeyboardButton('Ванкомицин')
            butt6 = types.KeyboardButton('Ципрофлоксацин')
            butt7 = types.KeyboardButton('Сульперазон')
            butt8 = types.KeyboardButton('Цефтриаксон')
            butt9 = types.KeyboardButton('Максиктам')
            butt10 = types.KeyboardButton('Имипинем-циластатин')
            butt11 = types.KeyboardButton('Меропенем')
            butt12 = types.KeyboardButton('Ко-тримоксазол')
            butback = types.KeyboardButton('В начало')
            markup.add(butt1, butt2, butt3, butt4, butt5, butt6, butt7, butt8, butt9, butt10, butt11, butt12, butback)
            bot.send_message(message.chat.id, 'Выберите нужный антибиотик'.format(message.from_user),reply_markup=markup)
        elif message.text == 'Ампициллин+сульбактам':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bot.send_message(message.chat.id, 'Ампициллин+Сульбактам\n'
                                              '(Сультасин, Амписид)\n'
                                              'Недоношенным и доношенным\n'
                                              'до 1 недели - 75мг/кг*сут.\n'
                                              'Доношенным старше 1 недели\n'
                                              '150мг/кг*сут.\n'
                                              '1500мг - 10мл\n'
                                              '10:00, 22:00\n'
                                              '2 раза в день\n'
                                              'до 14 дней')
        elif message.text == 'Амикацин':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bot.send_message(message.chat.id, 'Амикацин.\n'
                                              'Недоношенные начальная доза\n'
                                              '10мг/кг, затем 7.5мг/кг\n'
                                              'каждые 24 часа (1р/сут).\n'
                                              'Доношенные начальная доза\n'
                                              '10мг/кг, затем 7.5мг/кг\n'
                                              'каждые 12 часов (2р/сут).\n'
                                              '500мг - 5мл\n'
                                              '7 - 10 дней\n'
                                              'Конечная концентрация 5мг/мл')
        elif message.text == 'Гентамицин':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bot.send_message(message.chat.id, 'Гентамицин.\n'
                                              'До 36 нед. включительно и\n'
                                              'тяжёлая асфиксия - 4мг/кг\n'
                                              '>= 37 нед. - 5мг/кг\n'
                                              '40мг - 1мл\n'
                                              '1р/сут\n'
                                              'до 7 дней\n'
                                              'Off Label до 1 мес.\n'
                                              'Конечная концентрация 1мг/мл')
        elif message.text == 'Ванкомицин':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bot.send_message(message.chat.id, 'Ванкомицин (Эдицин)\n'
                                              'Начальная доза 15мг/кг.\n'
                                              'Затем в 1ю неделю: 10мг/кг *2р/сут\n'
                                              'Со 2й недели: 10мг/кг *3р/сут\n'
                                              'От 1 месяца: 10мг/кг *4р/сут\n'
                                              '500мг - 10мл\n'
                                              'до 14 дней\n'
                                              'Конечная концентрация 5мг/мл\n'
                                              'При ОПН уменьшить интервал введения')
        elif message.text == 'Цефтриаксон':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bot.send_message(message.chat.id, 'Цефтриаксон\n'
                                              'До 2х недель 50мг/кг\n'
                                              'От 2х недель 80мг/кг\n'
                                              'При менингитах 100мг/кг\n'
                                              '100мг - 1мл\n'
                                              '15:00\n'
                                              '1р/сут\n'
                                              'от 4 до 14 дней')
        elif message.text == 'Имипинем-циластатин':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bot.send_message(message.chat.id, 'Имипинем-циластатин (Тиенам, Бактопенем)\n'
                                              '60мг/кг*сут\n'
                                              '4р/сут\n'
                                              '500мг - 100мл\n'
                                              'Длительность индивидуально\n'
                                              'Off Label до 3 мес.\n'
                                              'Конечная концентрация 5мг/мл')
        elif message.text == 'Ко-тримоксазол':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bot.send_message(message.chat.id, 'Ко-тримоксазол (Бисептол)\n'
                                              '36мг/кг*сут (30+6)\n'
                                              '96мг (80+16) - 1мл\n'
                                              '2р/сут\n'
                                              '5-14 дней\n'
                                              'Off Label +\n'
                                              'Конечная концентрация 25мг/мл\n'
                                              'Инфузия 60-90мин.')
        elif message.text == 'Сульперазон':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bot.send_message(message.chat.id, 'Сульперазон (Цефоперазон-Сульбактам\n,'
                                              'Сульзонцеф, Сульмаграф)\n'
                                              '40-80мг/кг*сут\n'
                                              'При серъёзных инфекциях\n'
                                              'до 160мг/кг*сут\n'
                                              '250мг - 1мл\n'
                                              '2р/сут\n'
                                              'до 14 дней\n'
                                              'Конечная концентрация 100мг/мл')
        elif message.text == 'Тазоцин':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bot.send_message(message.chat.id, 'Тазоцин (Тациллин Дж,\n'
                                              'Пиперациллин-Тазобактам)\n'
                                              '50-100мг\n'
                                              '<29нед 0-28 дней - 2р/сут\n'
                                              'старше 28 дней - 3р/сут\n'
                                              '30-36нед 0-14 дней - 2р/сут\n'
                                              'старше 14 дней - 3р/сут\n'
                                              '37-44нед до 7 дней - 2р/сут\n'
                                              'После 45 нед ПКВ - 3р/сут\n'
                                              '200мг - 1мл\n'
                                              'Off Label +\n'
                                              'Конечная концентрация 50мг/мл')
        elif message.text == 'Ципрофлоксацин':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bot.send_message(message.chat.id, 'Ципрофлоксацин\n'
                                              '10мг/кг\n'
                                              '2мг - 1мл\n'
                                              '3р/сут\n'
                                              '10-14 дней\n'
                                              'Off Label +')
        elif message.text == 'Максиктам':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bot.send_message(message.chat.id, 'Максиктам (Цефепим+Сульбактам)\n'
                                              '50мг/кг по Цефепиму\n'
                                              '1000мг - 1мл\n'
                                              '2р/сут\n'
                                              '10 дней\n'
                                              'Off Label + до 2х мес.\n'
                                              'Конечная концентрация 40мг/мл')
        elif message.text == 'Меропенем':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bot.send_message(message.chat.id, 'Меропенем\n'
                                              '10-20мг/кг\n'
                                              '1000мг - 20мл\n'
                                              '3р/сут\n'
                                              'Off Label + до 3х мес.\n'
                                              'Конечная концентрация 20мг/мл')

        elif message.text == 'Миорелаксанты':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            butt1 = types.KeyboardButton('Пипекурония бромид (ардуан)')
            butt2 = types.KeyboardButton('Атракурия безилат')
            butt3 = types.KeyboardButton('Рокурония бромид')
            butback = types.KeyboardButton('В начало')
            markup.add(butt1, butt2, butt3, butback)
            bot.send_message(message.chat.id, 'Выберите нужный миорелаксант'.format(message.from_user),reply_markup=markup)
        elif message.text == 'Пипекурония бромид (ардуан)':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bot.send_message(message.chat.id, 'Пипекурония бромид\n'
                                              '(Ардуан, Веро-пипекуроний)\n'
                                              'разово 40мкг/кг\n'
                                              'титрование 10-20мкг/кг*ч\n'
                                              'Длительный. Кардиодепрессивное действие')
        elif message.text == 'Атракурия безилат':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bot.send_message(message.chat.id, 'Атракурия безилат (Тракриум)\n'
                                              'разово 0.3-0.6мг/кг\n'
                                              'титрование 0.3-0.6мг/кг*ч\n'
                                              'Средний. Можно при ОПН')
        elif message.text == 'Рокурония бромид':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bot.send_message(message.chat.id, 'Рокурония бромид (Эсмерон)\n'
                                              'разово 0.6мг/кг\n'
                                              'титрование 0.3-0.6мг/кг*ч\n'
                                              'Короткий или средний')

        elif message.text == 'Анальгоседация':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            butt1 = types.KeyboardButton('Фентанил')
            butt2 = types.KeyboardButton('Промедол')
            butt3 = types.KeyboardButton('Кетамин')
            butt4 = types.KeyboardButton('Трамадол')
            butt5 = types.KeyboardButton('Диазепам')
            butt6 = types.KeyboardButton('Мидазолам')
            butt7 = types.KeyboardButton('Натрия оксибутират')
            butback = types.KeyboardButton('В начало')
            markup.add(butt1, butt2, butt3, butt4, butt5, butt6, butt7, butback)
            bot.send_message(message.chat.id, 'Выберите нужный анальгетик'.format(message.from_user),reply_markup=markup)
        elif message.text == 'Фентанил':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bot.send_message(message.chat.id, 'Фентанил\n'
                                              '0.25-3мкг/кг каждые 4-6ч\n'
                                              'длительность 2-4 часа\n'
                                              'капельно 1-10мкг/кг*ч\n'
                                              'Влияет на дыхательный центр')
        elif message.text == 'Промедол':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bot.send_message(message.chat.id, 'Промедол\n'
                                              '0.05-0.2мг/кг\n'
                                              'в течение 10минут\n'
                                              'каждые 4-6 часов\n'
                                              'длительность 2-4 часа\n'
                                              'капельно 0.1-0.2мкг/кг*ч')
        elif message.text == 'Кетамин':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bot.send_message(message.chat.id, 'Кетамин\n'
                                              '0.5мг/кг каждые 15-30мин\n'
                                              'длительность 0.5 часа\n'
                                              'капельно 500-1000мкг/кг*ч\n'
                                              '*Александрович')
        elif message.text == 'Трамадол':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bot.send_message(message.chat.id, 'Трамадол\n'
                                              'разово 1-2мг/кг\n'
                                              'капельно 0.1-0.2мг/кг*ч')
        elif message.text == 'Диазепам':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bot.send_message(message.chat.id, 'Диазепам (Реланиум)\n'
                                              'разово 0.1-0.3мг/кг\n'
                                              'капельно 0.1-0.2мг/кг*ч\n'
                                              'Инфузия на воде для инъекций')
        elif message.text == 'Мидазолам':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bot.send_message(message.chat.id, 'Мидазолам\n'
                                              'разово 0.05(0.1)-0.2(0.5)мг/кг\n'
                                              'в течение 5 минут\n'
                                              'капельно: >32 недель\n'
                                              '0.03мг/кг*ч (0.05мкг/кг*мин)\n'
                                              '<32 недель\n'
                                              '0.06мг/кг*ч (1мкг/кг*мин)\n'
                                              '0.1-0.3мг/кг*ч (по Рооз)\n'
                                              'Off Label до 3х месяцев')
        elif message.text == 'Натрия оксибутират':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bot.send_message(message.chat.id, 'Натрия оксибутират\n'
                                              'разово 50-100мг/кг\n'
                                              'капельно 20-60мг/кг*ч\n'
                                              'В качестве противосудорожной терапии')

        elif message.text == 'Противогрибковые/вирусные':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            butt1 = types.KeyboardButton('Флуконазол')
            butt2 = types.KeyboardButton('Амфотерицин В')
            butt3 = types.KeyboardButton('Ацикловир')
            butback = types.KeyboardButton('В начало')
            markup.add(butt1, butt2, butt3, butback)
            bot.send_message(message.chat.id, 'Выберите нужный противогрибковый/вирусный препарат'.format(message.from_user),reply_markup=markup)
        elif message.text == 'Флуконазол':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bot.send_message(message.chat.id, 'Флуконазол (Дифлюкан)\n'
                                              'профилактическая 5мг/кг *1р/3дня\n'
                                              'лечебная 12мг/кг *1р/сут\n'
                                              '2мг - 1мл\n'
                                              'в/в капельно за 30-60мин')
        elif message.text == 'Амфотерицин В':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bot.send_message(message.chat.id, 'Амфотерицин В\n'
                                              '20мг/кг\n'
                                              '5мг - 1мл (5000 ЕД - 1мл)\n'
                                              '1р/сут в течение 2-6 часов\n'
                                              'до 20 дней\n'
                                              'Конечная концентрация 0.1мг/мл\n'
                                              'Разводится на 5% глюкозе')
        elif message.text == 'Ацикловир':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bot.send_message(message.chat.id, 'Ацикловир\n'
                                              '20мг/кг\n'
                                              '25мг - 1мл\n'
                                              '3р/сут\n'
                                              '14-21 день\n'
                                              'Off Label +')

        elif message.text == 'Общий анализ крови':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            butt1 = types.KeyboardButton('Общий анализ')
            butt2 = types.KeyboardButton('Лейкоформула')
            butt3 = types.KeyboardButton('Красная кровь')
            butback = types.KeyboardButton('В начало')
            markup.add(butt1, butt2, butt3, butback)
            bot.send_message(message.chat.id, 'Выберите нужный анализ крови'.format(message.from_user), reply_markup=markup)
        elif message.text == 'Общий анализ':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            photo = open('Pictures/OAK.png', 'rb')
            bot.send_photo(message.chat.id, photo)
        elif message.text == 'Лейкоформула':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            photo = open('Pictures/Leicoformula.png', 'rb')
            bot.send_photo(message.chat.id, photo)
        elif message.text == 'Красная кровь':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            photo = open('Pictures/RedBlood.png', 'rb')
            bot.send_photo(message.chat.id, photo)

        elif message.text == 'Анализ ликвора':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            butt1 = types.KeyboardButton('Ликвор по Рооз')
            butt2 = types.KeyboardButton('Ликвор по сроку гестации')
            butback = types.KeyboardButton('В начало')
            markup.add(butt1, butt2, butback)
            bot.send_message(message.chat.id, 'Выберите нужный анализ ликвора'.format(message.from_user), reply_markup=markup)
        elif message.text == 'Ликвор по Рооз':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            photo = open('Pictures/Cerebrospin Roos.png', 'rb')
            bot.send_photo(message.chat.id, photo)
        elif message.text == 'Ликвор по сроку гестации':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            photo = open('Pictures/Cerebrospin Nedon.png', 'rb')
            bot.send_photo(message.chat.id, photo)

        elif message.text == 'БЛД':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            butt1 = types.KeyboardButton('Гормональная терапия при БЛД')
            butback = types.KeyboardButton('В начало')
            markup.add(butt1, butback)
            bot.send_message(message.chat.id, 'Что вы хотите посмотреть по БЛД?'.format(message.from_user),reply_markup=markup)
        elif message.text == 'Гормональная терапия при БЛД':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            butt1 = types.KeyboardButton('10 дней')
            butt2 = types.KeyboardButton('21 день')
            butt3 = types.KeyboardButton('Кортеф')
            butt4 = types.KeyboardButton('БЛД')
            markup.add(butt1, butt2, butt3, butt4)
            bot.send_message(message.chat.id, 'Выберите гормональный курс при БЛД'.format(message.from_user),reply_markup=markup)
        elif message.text == '10 дней':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bot.send_message(message.chat.id, 'проект протокола, журнал Неонатология\n'
                                              '1-3 день - 0.15мг/кг*сут\n'
                                              '4-6 день - 0.1мг/кг*сут\n'
                                              '7-8 день - 0.05мг/кг*сут\n'
                                              '9-10 день - 0.02мг/кг*сут\n'
                                              'на 2 введения\n'
                                              'Курсовая доза 0.89мг/кг')
        elif message.text == '21 день':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bot.send_message(message.chat.id, 'Общий курс 21 день\n'
                                              '№1.1-2 день - 0.25мг/кг*сут\n'
                                              '№2.3-4 день - 0.135мг/кг*сут\n'
                                              '№3.5-6 день - 0.108мг/кг*сут\n'
                                              '№4.7-8 день - 0.086мг/кг*сут\n'
                                              '№5.9-10 день - 0.077мг/кг*сут\n'
                                              '№6.11-12 день - 0.069мг/кг*сут\n'
                                              '№7.ещё 7 дней - 0.05мг/кг*сут\n'
                                              'на 2 введения')
        elif message.text == 'Кортеф':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bot.send_message(message.chat.id, 'Кортеф\n'
                                              '1-3 день - 2мг/кг*сут на 2 приёма\n'
                                              '4-6 день - 1мг/кг*сут на 2 приёма\n'
                                              '6-10 день - 1мг/кг*сут через день')

        elif message.text == 'Метаболические нарушения':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            butt1 = types.KeyboardButton('Обмен кальция')
            butt2 = types.KeyboardButton('Обмен глюкозы')
            butback = types.KeyboardButton('В начало')
            markup.add(butt1, butt2, butback)
            bot.send_message(message.chat.id, 'Что вы хотите посмотреть про особенности метаболизма?'.format(message.from_user),reply_markup=markup)
        elif message.text == 'Обмен кальция':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            photo = open('Pictures/Kalcii_norma.jpg', 'rb')
            bot.send_photo(message.chat.id, photo)
            bot.send_message(message.chat.id, 'Соотношение величин.\n'
                                              '1ммоль/л - 4мг/дл\n'
                                              '1мэкв - 20мг\n'
                                              '1мэкв/л - 0.5ммоль/л')
            bot.send_message(message.chat.id, 'В парентеральном питании.\n'
                                              'Начало с 1х суток.\n'
                                              'По кальция глюконату 10%.\n'
                                              '4.4мл CaGluc = 1ммоль Ca\n'
                                              '1-2-3мл/кг*сут\n'
                                              '2-4мл/кг*сут для ЭНМТ')
            butt1 = types.KeyboardButton('Гипокальциемия')
            butt2 = types.KeyboardButton('Гиперкальциемия (в работе)')
            butt3 = types.KeyboardButton('Метаболические нарушения')
            markup.add(butt1, butt2, butt3)
            bot.send_message(message.chat.id, 'Какой вид нарушения кальция?'.format(message.from_user), reply_markup=markup)
        elif message.text == 'Гипокальциемия':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            photo = open('Pictures/GipoKalcii_algoritm.jpg', 'rb')
            bot.send_photo(message.chat.id, photo)
            bot.send_message(message.chat.id, 'Содержание ионизированного кальция в растворах.\n'
                                              'Кальция хлорид 10% - 36мг/мл\n'
                                              'Кальция глюконат 10% - 9мг/мл\n'
                                              'Кальция лактат 10% - 13мг/мл')
            bot.send_message(message.chat.id, 'Бессимптомная гипокальциемия.'
                                              'Недоношенным. Кальция глюконат 10%.\n'
                                              '5-10мл/сут внутрь или 1-2мл/кг в/в\n'
                                              'Гипокальциемия.\n'
                                              '<1ммоль/л при m> 1500г или <0.8ммоль при m< 1500г\n'
                                              'В/в инфузия 40-50мг/кг*сут, но доза\n'
                                              'больше 20-30мг/кг*сут - много нежелательных эффектов.\n'
                                              'Гипокальциемия с клиникой (судоророги, нарушения ритма)\n'
                                              'Болюсно Кальция глюконат 1-2мл/кг\n'
                                              'Максимум: 5.0мл для недоношенных, 10.0мл для доношенных\n'
                                              'Скорость не более 1мл/мин')

        elif message.text == 'Обмен глюкозы':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            photo = open('Pictures/Glucosa_Potrebnost.png', 'rb')
            bot.send_photo(message.chat.id, photo)
            butt1 = types.KeyboardButton('Гипогликемия')
            butt2 = types.KeyboardButton('Гипергликемия')
            butt3 = types.KeyboardButton('Метаболические нарушения')
            markup.add(butt1, butt2, butt3)
            bot.send_message(message.chat.id, 'Какой вид нарушения глюкозы?'.format(message.from_user), reply_markup=markup)
        elif message.text == 'Гипогликемия':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bot.send_message(message.chat.id, 'Гипогликемия - меньше <b>2.6ммоль/л</b>\n'
                                              '1. Ранняя неонатальная (первые 6-12ч). ЗВУР, матери с СД, '
                                              'тяжёлая ГБН, асфиксия.\n'
                                              '2. Транзиторная (12-48ч). Недоношенные, ЗВУР, близнецы, '
                                              'полицитемия.\n'
                                              '3. Вторичная (любой возраст). Сепсис, нарушением терморежима, '
                                              'ятрогения, поражение ЦНС, кровоизлияние в надпочечники, матери- '
                                              'антидиабетические препараты, глюкокортикоиды, салицилаты.\n'
                                              '4. Персистирующая (после 7 суток).', parse_mode='html')
            bot.send_message(message.chat.id, 'Коррекция гипогликемии:\n'
                                              '1. Глюкоза 2-4мл/кг 20% или, лучше, 4-8мл/кг 10% '
                                              'со скоростью не более 1.0мл/мин за 5 минут. Затем переход '
                                              'на постоянную инфузию 10% 2.4-4.6мл/кг*ч (4-8мг/кг*мин) '
                                              'по потребности. Контроль через 30 минут.\n'
                                              '2. Постоянная инфузия 6-8мкг/кг*мин 10% глюкозы. '
                                              'Второй способ дольше, но более плавный.\n'
                                              'При сохранении гипогликемии - скорость повышается до 10мл/кг*ч 10% глюкозы.\n'
                                              'При продолжении сохранения гипогликемии - контринсулярная терапия.\n'
                                              'Глюкагон (0.1-0.5мг/кг в/м *2р/сут)\n'
                                              'Гидрокортизон (5-10мг/кг*сут) или преднизолон (2-3мг/кг*сут)')
        elif message.text == 'Гипергликемия':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            photo = open('Pictures/Glucosa_Giperglicemia.png', 'rb')
            bot.send_photo(message.chat.id, photo)

        elif message.text == 'Гипотермия':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bot.send_message(message.chat.id, 'В основе - клинические рекомендации 2019г\n'
                                              'Р21.0 Тяжёлая асфиксия при рождении\n'
                                              'Р91.0 Церебральная ишемия')
            butt1 = types.KeyboardButton('Показания к гипотермии')
            butt2 = types.KeyboardButton('Противопоказания к гипотермии')
            butt3 = types.KeyboardButton('Действия на этапе роддома')
            butt4 = types.KeyboardButton('Этап согревания')
            butt5 = types.KeyboardButton('Экстренное прекращение гипотермии')
            butt6 = types.KeyboardButton('Обследования при гипотермии')
            butt7 = types.KeyboardButton('Целевые витальные показатели при гипотермии')
            butt8 = types.KeyboardButton('Особенности проведения гипотермии')
            butback = types.KeyboardButton('В начало')
            markup.add(butt1, butt2, butt3, butt4, butt5, butt6, butt7, butt8, butback)
            bot.send_message(message.chat.id, 'Что вы хотите посмотреть про гипотермию?'.format(message.from_user),reply_markup=markup)
        elif message.text == 'Показания к гипотермии':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bot.send_message(message.chat.id, 'Хотя бы один критерий в каждой группе!\n'
                                              'Критерии А\n'
                                              '- Апгар <=5 на 10й мин. или\n'
                                              '- сохраняется потребность в ИВЛ на 10й мин. или\n'
                                              '- в первом анализе до 60мин. рН < 7.0 или\n'
                                              '- в первом анализе до 60мин. (ВЕ) >= 16моль/л\n'
                                              'Критерии В\n'
                                              '- клинически выраженные судороги или\n'
                                              '- мышечная гипотония и гипорефлексия или\n'
                                              '- выраженный гипертонус и гипорефлексия или\n'
                                              '- нарушения зрачкового рефлекса (реакция на свет)\n'
                                              'Критерии С\n'
                                              '- показатели на ЭЭГ (опущены по тех.причине, показания оцениваются '
                                              'только по критериям групп А и В)\n')
        elif message.text == 'Противопоказания к гипотермии':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bot.send_message(message.chat.id, '- масса менее 1800г, гестационный возраст менее 35нед\n'
                                              '- возраст на момент принятия решения больше 6 часов\n'
                                              '- тяжёлые ВПР, требующие срочного хир. вмешательства\n'
                                              '- тяжёлые ВПР несовместимые с жизнью\n'
                                              '- выявление при обследовании внутричерепного кровоизлияния. При подозрении '
                                              'целесообразно провести КТ/МРТ до начала гипотермии\n'
                                              '- отказа от проведения процедуры законных представителей.')
        elif message.text == 'Действия на этапе роддома':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bot.send_message(message.chat.id, '- контроль КЩС крови в первые 60мин\n'
                                              '- установка ректального термодатчика (диаметр 2мм, глубина 5см)\n'
                                              '- начать гипотермию до 33.5-34.0С, контроль каждые 15мин, время '
                                              'достижения целевых цифр 60мин\n'
                                              '- открытая система, кожа открыта, подгузник подложен, но не застёгнут\n'
                                              '- при необходимости доп.охлаждения - исключить прямой контакт с кожей (5-15см)\n'
                                              '- провести НСДГ, ЭЭГ при тех.возможности\n'
                                              '- при отсутствии показаний - прекратить и постепенно согреть 0.5С/час')
        elif message.text == 'Этап согревания':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bot.send_message(message.chat.id, 'Гипотермия проводится в течение 72 часов.\n'
                                              '- согревание 0.3-0.5С/час до ректальной 37С. (7-9часов)\n'
                                              '- при экстренном прекращении гипотермии - скорость та же\n'
                                              '- контроль ректальной температуры - ещё в течение 24часов\n'
                                              '- судороги при согревании - прекратить согревание, провести '
                                              'противосудорожную терапию, продолжить согревать не ранее, чем '
                                              'через 2 часа после прекращения судорог\n'
                                              '- согревание - возможно: вазодилятация -> гипотензия. Коррекция 10мл/кг Nacl 0.9%')
        elif message.text == 'Экстренное прекращение гипотермии':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bot.send_message(message.chat.id, '- невозможность скорректировать гипоксемию (SpO2 менее 90%)\n'
                                              '- признаки жизнеугрожающей коагулопатии, не коррегируется стандартной терапией\n'
                                              '- выявление внутричерепного кровоизлияния\n'
                                              '- тяжёлые, некупирующиеся нарушения сердечного ритма\n'
                                              '- стойкие гемодинамические нарушения, которые не купируются восполнением ОЦК '
                                              'и применением инотропных препаратов')
        elif message.text == 'Обследования при гипотермии':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bot.send_message(message.chat.id, 'Приказ Минздрава от 10.05.2017 №203н\n'
                                              'При поступлении в ОРИТН:\n'
                                              '- лаборатория: ОАК, ОАМ, БХ, КЩС, глюкоза, коагулограмма, бак.исследования\n'
                                              '- НСГ, R-графия, ЭхоКГ\n'
                                              '- оценка по Sarnat в модификации Stoll B., Kliegmann (2004)\n'
                                              'После окончания гипотермии:\n'
                                              '- НСГ 3, 7-10сут\n'
                                              '- МРТ 14-21сут')
            photo = open('Pictures/Klassif GIE Kliegmann.png', 'rb')
            bot.send_photo(message.chat.id, photo)
        elif message.text == 'Целевые витальные показатели при гипотермии':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bot.send_message(message.chat.id, 'Сопутствующую интенсивную терапию проводить по общепринятым правилам.\n'
                                              '- среднее АД 45-65мм.рт.ст.\n'
                                              '- SpO2 - 90-95%\n'
                                              '- Р СО2 - 35-55 мм.рт.ст.\n'
                                              '- Р О2 - 60-80 мм.рт.ст.\n'
                                              '- электролиты, глюкоза в пределах нормы\n'
                                              '- ЧСС 80-120. При снижении ниже 80 - исключить избыточную седацию')
        elif message.text == 'Особенности проведения гипотермии':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bot.send_message(message.chat.id, '- смена положения каждые 6 часов\n'
                                              '- ИВЛ не обязательное условие\n'
                                              '- гипо и гиперкапния одинаково опасны как повреждающие мозг факторы\n'
                                              '- гемодинамическая терапия по общепринятым правилам, АД выше целевых значений\n'
                                              '- стартовая инфузия 60мл/кг*сут\n'
                                              '- при отсутствии противопоказаний возможно как парентеральное так и '
                                              'энтеральное питание по протоколу\n'
                                              '- гипотермия - не показание к АБ-терапии, при необходимости - пенициллины + '
                                              'аминогликозиды\n'
                                              '- показание к противосудорожной терапии - судороги или изменения на ЭЭГ\n'
                                              '- показание к наркотическим анальгетикам - наличие дрожи\n'
                                              '- снижение температуры тела на 3.5С в среднем на 30% снижает коагуляцию, '
                                              'не требует лечения в отсутствии кровоточивости, при наличии - СЗП')

        elif message.text == 'ГБН. Желтуха':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bot.send_message(message.chat.id, 'В основе - клинические рекомендации 2016 и 2017гг\n'
                                              'Р55.0 Резус-изоиммунизация плода и новорожденного\n'
                                              'Р55.1 АВ0-изоиммунизация плода и новорожденного\n'
                                              'Р55.8 Другие формы ГБП и ГБН\n'
                                              'Р56.0 Водянка плода, обусловленная изоиммунизацией\n'
                                              'Р57.0 Ядерная желтуха, обусловленная изоиммунизацией\n'
                                              'Р59.0 Неонатальная желтуха, связанная с преждевременным родоразрешением\n'
                                              'Р59.9 Неонатальная желтуха неуточнённая\n'
                                              'Гипербилирубинемия - повышение билирубинa в сыворотке крови\n'
                                              '>256мкмоль/л при ГВ больше 35 нед\n'
                                              '>171мкмоль/л при ГВ меньше 35 нед\n'
                                              'Визуально: >67мкмоль/л у доношенных, >120мкмоль/л у недоношенных')
            butt1 = types.KeyboardButton('Билирубиновая энцефалопатия')
            butt2 = types.KeyboardButton('Методы исследования при желтухах')
            butt3 = types.KeyboardButton('ГБН по степени тяжести')
            butt4 = types.KeyboardButton('ГБН 1е сутки тактика')
            butt5 = types.KeyboardButton('Фототерапия при желтухе')
            butt6 = types.KeyboardButton('ОЗПК (операция заменного переливания крови)')
            butback = types.KeyboardButton('В начало')
            markup.add(butt1, butt2, butt3, butt4, butt5, butt6, butback)
            bot.send_message(message.chat.id, 'Что вы хотите посмотреть про желтуху новорожденных?'.format(message.from_user),reply_markup=markup)
        elif message.text == 'Билирубиновая энцефалопатия':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bot.send_message(message.chat.id, 'I фаза: нарастание интоксикации. Угнетение: апноэ, апатия, монотонный крик, срыгивания. '
                                              'Обычно 4й день жизни. При ОЗПК - изменения обратимы\n'
                                              'II фаза: спастическая. Спастичность, ригидность затылочных мышц, опистотонус, мозговой крик, '
                                              'крупноразмашистый тремор, нистагм, апноэ, летаргия, судороги. Дни-недели. Поражения ЦНС необратимы.\n'
                                              'I и II - острая билирубиновая энцефалопатия. У глубоконедоношенных маскируется другой патологией.\n'
                                              'III фаза: ложного благополучия (2-3 мес.). Полное или частичное исчезновение спастичности.\n'
                                              'IV фаза: формирование неврологических осложнений (после 3-5мес.). Парезы, параличи, атетоз, '
                                              'глухота, ДЦП, задержка психического развития.')
            photo = open('Pictures/Bilirubin Encefalopatia.png', 'rb')
            bot.send_photo(message.chat.id, photo)
        elif message.text == 'Методы исследования при желтухах':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bot.send_message(message.chat.id, 'Визуальная оценка - шкала Крамера. У доношенных, с нормальной массой тела.')
            photo = open('Pictures/Zeltuha Kramer.png', 'rb')
            bot.send_photo(message.chat.id, photo)
            bot.send_message(message.chat.id, 'Транскутанное измерение.\n'
                                              'Прямая зависимость с уровнем в крови от 100 до 255мкмоль/л.\n'
                                              'Только в области лба или грудины.\n'
                                              'Не используется после начала фототерапии.\n'
                                              'Только при ГВ более 35 недель.')
            bot.send_message(message.chat.id, 'Стандартное исследование Бр крови.\n'
                                              '- Всем с желтухой, менее 35 нед.\n'
                                              '- Всем с проявлением желтухи в первые 24 часа\n'
                                              '- С признаками ГБН или другими рисками патологической желтухи\n'
                                              '- Больше 35нед, если транскутанно: >140 в возрасте 24-48ч\n'
                                              '>200 в возрасте 48-72ч\n'
                                              '>250 в возрасте старше 72ч\n'
                                              '- Всем, получающим фототерапию (каждые 12-24ч)')
            bot.send_message(message.chat.id, 'Проба Кумбса. При Rh-отрицат. крови матери. Прямая проба из крови пуповины.\n'
                                              'Положительная при ГБН по Rh-фактору. При ГБН по АВ0 чаще слабо+ в 1сут и '
                                              'негативная через 2-3дня.\n'
                                              'Непрямая. Более чувствительный тест на выявление материнских изоантител.\n'
                                              'Выраженность реакции не коррелирует с тяжестью состояния!')
            bot.send_message(message.chat.id, 'Исследование ретукулоцитов.\n'
                                              'Обычно повышается при ГБН - компенсаторная реакция на гемолиз.\n'
                                              'Доношенные - 4-7% (200.000-400.000/mL)\n'
                                              'Недоношенные - 6-10% (400.000-550.000/mL)\n'
                                              'К 4 дню снижается до 1% (50.000/mL)\n'
                                              'При ГБН - 10-40%')
        elif message.text == 'ГБН по степени тяжести':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bot.send_message(message.chat.id, 'Желтушная форма - степень тяжести по анализу пуповинной крови.\n'
                                              'Лёгкое течение:\n'
                                              'Hb - более 140г/л, Бр - менее 68мкмоль/л\n'
                                              'Начало на 1-2сут. Почасовой прирост 4-5мкмоль/л\n'
                                              'Для лечения может только фототерапия.\n'
                                              'Средняя степень:\n'
                                              'Hb - 100-140г/л, Бр - 68-85мкмоль/л\n'
                                              'Начало в первые часы. Почасовой прирост 6-10мкмоль/л\n'
                                              'Интенсивная фототерапия, часто ОЗПК.\n'
                                              'Тяжёлая степень соответствует отёчной ГБН, внутриутробно по УЗИ:\n'
                                              'Hb - менее 100г/л, Бр - более 85мкмоль/л\n'
                                              'Может быть ДН, нарушение ССС, Бр-энцефалопатия, шок, геморрагический с-м.')
        elif message.text == 'ГБН 1е сутки тактика':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bot.send_message(message.chat.id, '* Наблюдение - оценка состояния по величине почасового прироста.\n'
                                              '* Готовиться к ОЗПК - заказать кровь+СЗП, стабилизировать '
                                              'жизненно-важные функции')
            photo = open('Pictures/GBN_Tactic_1day.png', 'rb')
            bot.send_photo(message.chat.id, photo)
        elif message.text == 'Фототерапия при желтухе':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bot.send_message(message.chat.id, 'Комбинированная фототерапия (2 и более источников), хотя бы при одном признаке:\n'
                                              '- почасовой прирост ОБС > 6.8мкмоль/л*час\n'
                                              '- через 72ч уровень ОБС менее 50мкмоль/л от порогового значения для ЗПК\n'
                                              '- через 6ч фототерапии уровень ОБС повышается или не снижается')
            photo = open('Pictures/Phototherapy_Massa.png', 'rb')
            bot.send_photo(message.chat.id, photo)
            photo = open('Pictures/Phototherapy_Gest.png', 'rb')
            bot.send_photo(message.chat.id, photo)
        elif message.text == 'ОЗПК (операция заменного переливания крови)':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bot.send_message(message.chat.id, 'Кровь и компоненты 150-170мл/кг для доношенных и 170-180мл/кг для недоношенных. '
                                              'Соотношение эр.массы/взвеси и  СЗП 2:1\n'
                                              'Первая порция на анализ билирубина.\n'
                                              'Объём одного замещения 10-20мл/кг для доношенных и 5-10мл/кг для недоношенных.\n'
                                              '3-4мл/мин. 2 шприца эр.массы/ 1 шприц СЗП.\n'
                                              'После каждых 100мл: 1-2мл 10% кальция глюконата в 5мл 5% глюкозы. Только между эр.массой!\n'
                                              'Перед окончанием - анализ на билирубин. Должно быть ниже в 2 раза.\n'
                                              'Кормить через 3-4 часа.\n'
                                              'Продолжить фототерапию.\n'
                                              'Контроль глюкозы через 1 час. Контроль билирубина через 12 часов.')
            photo = open('Pictures/OZPK_Massa.png', 'rb')
            bot.send_photo(message.chat.id, photo)
            photo = open('Pictures/OZPK_Gest.png', 'rb')
            bot.send_photo(message.chat.id, photo)

        elif message.text == 'Парентеральное питание':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bot.send_message(message.chat.id, 'В основе - протокол 2014г.\n'
                                              'Показано если ЭП не покрывает 90% от необходимого калоража и потребностей в питательных в-вах.\n'
                                              'Противопоказано на фоне реанимационных мероприятиях. Возобновление сразу после стабилизации.')
            photo = open('Pictures/Parenteral Pitanie Full Tab.png', 'rb')
            bot.send_photo(message.chat.id, photo)
            photo = open('Pictures/Parenteralnoe Pitanie Electrolit Full.png', 'rb')
            bot.send_photo(message.chat.id, photo)
            butt1 = types.KeyboardButton('Жидкость. Потребность')
            butt2 = types.KeyboardButton('Энергия. Потребность')
            butt3 = types.KeyboardButton('Белки. Потребность')
            butt4 = types.KeyboardButton('Жиры. Потребность')
            butback = types.KeyboardButton('В начало')
            markup.add(butt1, butt2, butt3, butt4, butback)
            bot.send_message(message.chat.id, 'Что вы хотите посмотреть про парентеральное питание?'.format(message.from_user),reply_markup=markup)
        elif message.text == 'Жидкость. Потребность':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bot.send_message(message.chat.id, 'Основная задача - обеспечение достаточной прибавки массы тела с 5-7 дня. ЭНМТ:18-21г/кг. >1500г: 14-15г/кг. Донош 7-8(до 14)г/кг.\n'
                                              'Физиологическая убыль массы не более 10%.\n'
                                              'Объём ЭП до 25мл/кг не учитывается\n'
                                              'Уровень Na поддерживается 135-145. Меньше - повреждние мозга, больше - ВЖК.\n'
                                              'Увеличение Na говорит о дегидратации. Увеличение - гипергидратация.\n'
                                              'ЭНМТ - с/м "поздней гипонатриемии" (нарушение почек и повышение потребления Na)')
            photo = open('Pictures/Parenteral Pitanie Zidkost.png', 'rb')
            bot.send_photo(message.chat.id, photo)
        elif message.text == 'Энергия. Потребность':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bot.send_message(message.chat.id, 'С первых суток обязательно Энергия покоя.\n'
                                              'Увеличение калорийности еждневно 10-15ккал/кг до 105ккал/кг к 7-10сут при полном ПП. Что соотв. 120ккал/кг при ЭП.\n'
                                              'При частичном ПП увеличение в том же темпе до 120ккал/кг к 7-10сут.\n'
                                              'Избыток небелковых калорий используется для синтеза жиров.')
            photo = open('Pictures/Parenteralnoe Pitanie Energy.png', 'rb')
            bot.send_photo(message.chat.id, photo)
        elif message.text == 'Белки. Потребность':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bot.send_message(message.chat.id, 'Основная задача - пластическая.\n'
                                              'Оценка достаточности: Антропометрия. Метаболические индексы (альбумин, мочевина, ацидоз). Индикаторный метод окисления АмК.\n'
                                              'Мочевина каждые 7-10д. Менее 1.8ммоль/л - недостаточность Б. Повышение может быть повышенный катаболизм Б при недостатки других.\n'
                                              'ОНМТ, ЭНМТ - 3г/кг*сут в первые 24ч безопасно и связано с лучшей прибавкой массы. Начать в первые часы.\n'
                                              'Альбумин, СЗП, компоненты крови - не являются источниками белка.\n'
                                              'Метаболический ацидоз - не противопоказание.\n'
                                              'Оптимальное соотношение белка и небелковых калорий от 4 до 2.5г/100ккал. От менее к более зрелым детям.')
        elif message.text == 'Жиры. Потребность':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bot.send_message(message.chat.id, 'Энергия. Созревание ГМ и сетчатки. Клеточные мембраны и сурфактант. Простогландины, лейкотриенты и др.медиаторы.\n'
                                              'При необходимости ограничения - не меньше 0.5-1г/кг*сут (дефицит эссенциальных кислот)\n'
                                              '1г - 10ккал. Защита инфузии от ультрафиолета, max близко, Ж-фильтр. Полное ПП - не более 3г/кг.\n'
                                              'Контроль - уровень триглицеридов (не выше 2.26ммоль/л (200мг/дл). При превышении снизить Ж на 0.5г/кг. Амфотерицин и '
                                              'глюкокортикоиды повышают конц.триглицеридов.')
            photo = open('Pictures/Parenteralnoe Pitanie Zhiri.png', 'rb')
            bot.send_photo(message.chat.id, photo)

        elif message.text == 'В начало':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            butt1 = types.KeyboardButton('Лекарства')
            butt2 = types.KeyboardButton('Лаборатория')
            butt3 = types.KeyboardButton('Патологии')
            butt4 = types.KeyboardButton('Быстрый доступ')
            markup.add(butt1, butt2, butt3, butt4)
            bot.send_message(message.chat.id, 'Чем могу помочь, {0.first_name}?'.format(message.from_user),reply_markup=markup)

    #bot.reply_to(message, message.text)


# RUN
bot.infinity_polling()