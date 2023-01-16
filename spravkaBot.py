import telebot
#import config
from telebot import types
TOKEN = '5984037791:AAGJacq-SfwcklPBWUNSEgguGxZuRby12qY' # bot token from @BotFather

bot = telebot.TeleBot(TOKEN)

def after_term():
    bot.send_message("Для начала работы со мной нажмите сюда - '/help'.")

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.reply_to(message, "Привет, я бот-справочник. У меня есть много разной полезной информации для врачей-реаниматологов. "
                          "Шучу, пока не очень много. Информация представлена в форме ветвящегося дерева - Вам достаточно просто "
                          "выбирать нужную кнопку.")
    bot.reply_to(message, "Слева есть меню, которое Вам подскажет, если что непонятно.")
    bot.reply_to(message, "Для начала работы со мной нажмите сюда - '/help'.")
    bot.reply_to(message, "Последние дополнения. АБ: Сульмаграф, Тазоцин, Ципрофлоксацин. Анализы: Общий крови, лейкоформула, красная кровь. "
                          "Анальгоседация: Фентанил, Промедол, Кетамин, Трамадол, Диазепам, Мидазолам, Натрия оксибутират. "
                          "Добавлен адрес для обратной связи.")

@bot.message_handler(commands=['connect'])
def welcome(message):
    bot.reply_to(message, "Если у вас возникли вопросы по работе бота или содержимому справочника (исправить или "
                          "предложить что добавить ещё и куда - то напишите мне на электронную почту с "
                          "соответствующей пометкой. Буду рад услышать конструктивные предложения. "
                          "kijiassa@gmail.com")

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
            item4 = types.KeyboardButton('Сердечные')
            item5 = types.KeyboardButton('Пероральные')
            butback = types.KeyboardButton('В начало')
            markup.add(item1, item2, item3, item4, item5, butback)
            bot.send_message(message.chat.id, 'Выберите группу препаратов'.format(message.from_user),reply_markup=markup)
        elif message.text == 'Лаборатория':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            butt1 = types.KeyboardButton('Общий анализ крови')
            butt2 = types.KeyboardButton('Биохимия')
            butt3 = types.KeyboardButton('Анализ ликвора')
            butt4 = types.KeyboardButton('Анализ мочи')
            butback = types.KeyboardButton('В начало')
            markup.add(butt1, butt2, butt3, butt4, butback)
            bot.send_message(message.chat.id, 'Выберите группу анализов'.format(message.from_user),reply_markup=markup)
        elif message.text == 'Патологии':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            butt1 = types.KeyboardButton('РДС')
            butt2 = types.KeyboardButton('Ишемия мозга')
            butt3 = types.KeyboardButton('Гемолитическая болезнь')
            butt4 = types.KeyboardButton('Аспирация мекония')
            butt5 = types.KeyboardButton('Хирургические патологии')
            butt6 = types.KeyboardButton('БЛД')
            butback = types.KeyboardButton('В начало')
            markup.add(butt1, butt2, butt3, butt4, butt5, butt6, butback)
            bot.send_message(message.chat.id, 'Выберите патологию'.format(message.from_user),reply_markup=markup)
        elif message.text == 'Антибиотики':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            butt1 = types.KeyboardButton('Амикацин')
            butt2 = types.KeyboardButton('Ампициллин+сульбактам')
            butt3 = types.KeyboardButton('Гентамицин')
            butt4 = types.KeyboardButton('Ванкомицин')
            butt5 = types.KeyboardButton('Цефтриаксон')
            butt6 = types.KeyboardButton('Тиенам')
            butt7 = types.KeyboardButton('Ко-тримоксазол')
            butt8 = types.KeyboardButton('Сульперазон')
            butt9 = types.KeyboardButton('Тазоцин')
            butt10 = types.KeyboardButton('Ципрофлоксацин')
            butback = types.KeyboardButton('В начало')
            markup.add(butt1, butt2, butt3, butt4, butt5, butt6, butt7, butt8, butt9, butt10, butback)
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
                                              'Off Label до 1 мес\n'
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
        elif message.text == 'Тиенам':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bot.send_message(message.chat.id, 'Тиенам (Имипинем-циластатин)\n'
                                              '60мг/кг*сут\n'
                                              '4р/сут\n'
                                              '500мг - 100мл\n'
                                              'Длительность индивидуально\n'
                                              'Off Label до 3 мес\n'
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

