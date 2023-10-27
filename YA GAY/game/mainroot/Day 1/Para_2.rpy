label D1P2_PERED_PAROY:
    if (sociofob > 0): 
        scene ODINOCHKA
        with dissolve
        play music "sounds/rinlab.ru-sound_07243.mp3"
        "~ Так-с аудитория 1-398 ~"
        "~ Ага, нашел! Вроде не опоздал ~"
        show GOGA_OUTSIDE at right2
        show BORYA_OUTSIDE at left2
        with dissolve
        "~ Хм, у этих ребят видимо, пара здесь же, может стоило подойти к ним? ~"
        window hide
        pause
        window show
        "~ Только их вроде было четверо ... ~"
        hide GOGA_OUTSIDE
        hide BORYA_OUTSIDE
        with dissolve
        pause
        "~ В любом случае времени на это уже нет ~"
        "~ Пора в аудиторию ~"
        hide ODINOCHKA
        scene PARA_KOMP
        with fade
        "Стас вошел в аудиторию"
        "В ней он снова увидел этих ребят"
        show GOGA_OUTSIDE at left2
        show BORYA_OUTSIDE at right2
        with dissolve
        g "О! Привет! Ты новенький?"
        "Стас неохотно подходит к ребятам"
        s "Д-да"
        b "Нам Серый говорил что к нам человечек со Школы Х переводится"
        g "Ага" 
        g "Как тебя зовут?"
        s "Станислав, можно просто - Стас"
        b "Очень приятно, я Боря, а это - Гоша"
        g "Привет"
        "Пожимают руки"
        "~ А они дружелюбные ~"
        "~ Но я не уверен что смогу влиться в этот коллектив так сразу ~"
        "~ Думаю мне нужно время, надо подумать ~" 
        "~ Эх{w}, ладно...надеюсь мы подружимся ~"
        g  "Стас, ты тут?"
        s "А? Что?"
        g "Я говорю, может расскажешь немного о себе?"
    else:
        scene PARA_KOMP
        play music "sounds/rinlab.ru-sound_07243.mp3"
        show GOGA_OUTSIDE at left2
        show BORYA_OUTSIDE at right2
        with dissolve
        g "Ну вроде успели"
        b "Отлично"
        g "Стас, может расскажешь немного о себе?"
        
    s "Х-xорошо, а конкретно что бы ты хотел узнать?"
    g "Хм, дай-ка подумать..."
    b "Давай я. Стас а ты с какого направления к нам перевелся то?"
    s "Я не знаю можно ли это назвать вообще направлением...в общем школа Х"
    s "Я со школы X"
    g "Ага, так-так-так, я смотрю оттуда многие бегут без оглядки"
    g "В других группах то же самое, как только чье-то место освободилось, то сразу обязательно кто-то займет его"
    b "Да, мне недавно знакомый с другой группы говорил, что к ним перевелся, мол, парень, который отлично учился и не подавал виду, что он хочет все бросить и уйти на другое направление"
    b "А вот спустя курс, уже в параллельной со мной группе"
    '~ Это он что так подразумевает меня что-ли? Только сказал что, якобы, "он" в параллельной группе и откуда ему известна моя успеваемость...  ~'
    "~ Так, Стас это что за выводы, зачем так раздувать то, успокойся ~"
    g "Эй, земля вызывает Стаса! Ау!"
    s "Ой! Извини, я просто задумался немного"
    b "Сейчас еще как задумаешься"
    s "Ты это о чем?"

    show GOGA_OUTSIDE at left
    show BORYA_OUTSIDE at left2
    with move
    show o_v at right
    stop music
    with dissolve
    o_v "Так, ребята."
    o_v "Все на места."
    o_v "Пара началась"
    jump D1P2



label D1P2:
    scene PARA_KOMP
    # play music....
    show o_v at center
    with dissolve
    o_v "Ну что же, давайте знакомиться"
    o_v "Зовут меня Ольга Владимировна"
    o_v "И давайте сразу обсудим организационные вопросы"
    stop music
    play sound "sounds/half-bathroom-door-knock_zy6lmond.mp3"
    o_v "Так, а кто это там?"
    hide o_v
    show DIVAN_SMILE at right2
    show ZHENYA_OUTSIDE at left2
    with dissolve
    d "..."
    z "..."
    o_v "И...может вы что-то скажете?"
    d "Простите за опоздание! Ольга..."
    z "...Владимировна"
    o_v "Чтобы больше такого не повторялось"
    d "Хорошо, простите"
    z "Извините"
    hide DIVAN_SMILE
    hide ZHENYA_OUTSIDE 
    with dissolve
    o_v "Я продолжу..."
    show o_v
    with dissolve
    o_v "Все-таки хоть вы уже и не самые маленькие в ВУЗе, но на пары ходить обязательно, вот до 3 курса дорастёте там уже видно будет"
    o_v "Это же и не обходит стороной и мои пары, посещение обязательное, если кто-либо прогулял, то пожалуйста предоставьте справку или иной документ, подтверждающий, что ваше отсутствие было уважительным"
    g "Ольга Владимировна!"
    o_v "Да я вас слушаю, простите просто пока еще не всех в лицо знаю, а что вы хотели?"
    g "Вот сразу узнать насчет автомата и есть ли он в принципе?"
    o_v "Так насчет автомата...он есть и это главное"
    o_v "А насчет получить автомат тут совсем другой вопрос"
    o_v "Во-первых необходима, как я уже говорила максимально возможная посещаемость, во-вторых это сдача всех 3 контрольных, а в-третьих это какая-никакая активность на практических занятиях"
    b "То есть это выходы к доске и ответы с места?"
    o_v "Да"
    g "А баллы за это будут?"
    o_v "Нет"
    stud "Оууу...почему...как так, а вот на матанализе как было вспомните"
    o_v "Ребят вы не на матанализе, и кстати за отказ от выхода к доске буду снимать баллы"
    "~ По-моему это несправедливо, даже в моей прежней школе и то давали бонусные баллы за активность, а не кормили завтраками, мол, тогда автомат поставим, бредятина какая-то ~"
    o_v "Так у кого-нибудь еще есть вопросы?"
    stud "..."
    o_v "Тогда давайте начнем вообще с введения в матлогику"
    o_v "А чему вас учила Елена Анатольевна на дискретке?"
    a "Ну получается у нас вот последняя тема была поиск в ширину и глубину, также было..."
    o_v "Я тебя перебью, извини, мне просто нужно понять что конкретно вы изучали по дискретке"
    o_v "У вас было упрощение логических выражений?"
    a "Конечно это одна из первых тем"
    o_v "Так это уже хороший разговор, давайте с этого и начнем, а там уже посмотрим по делу"
    "~ Хм...упростить логическое выражение, так она сказала? ~"
    o_v "Так я сейчас разберу простейший пример, а потом вызову одного человека к доске чтобы он упростил выражение с помощью элементарных преобразований"
    o_v "Итак, решаем: (x v y) -> (x v z)"
    window hide
    pause
    window show
    o_v "Так, и вот так упрощается это логическое выражение"
    o_v "Давайте я вызову одного человека к доске и он упростит следующее выражение"
    o_v "Ну так что кто готов?"
    "~ Может попробовать?... ~"
    window hide
    with dissolve
    menu:
        "Поднять руку":
            play music "music/PARA_HARD.mp3"
            $ uspevaemost += 1
            "~ Будь что будет ~"
            o_v "Так-так...О!"
            o_v "Новенький-готовенький получается сразу к бою?"
            s "Д-да...я просто хочу разобраться в этой теме"
            o_v "А что у вас там такого не было?"
            s "Ну вообще нет, но я примерно понимаю о чем речь"
            o_v "Хорошо, если что задавай вопросы"
            s "Спасибо"
            "Пример: (x v y) * (x v z) * x"
            hide o_v
            with dissolve
            window hide
            pause
            window show
            s "Простите, сразу такой вопрос, а как здесь скобка раскрывается?"
            o_v "Вот тебе таблица с формулами, с прошлого года у вас должны были они остаться в памяти, но раз уж у тебя не было такого, то прощаю"
            o_v "Но чтобы в следующий раз от зубов отскакивало"
            s "Хорошо, Спасибо!"
            window hide
            pause
            window show
            s "Так тут получается..."
            menu:
                "x":
                    "~ Вроде получается так ~"
                    show o_v at center
                    with dissolve
                    o_v "Так, ну что же и какой ответ?"
                    s "Я думаю это...{w}x?"
                    o_v "О! А говорил, что не знаешь, можешь когда захочешь!"
                    s "Да действительно"
                    o_v "Так, спасибо, присаживайся"
                    o_v "У кого-нибудь есть вопросы?"
                    stud "..."
                "x v y":
                    "~ Вроде получается так ~"
                    show o_v at center
                    with dissolve
                    o_v "Так, ну и какой же ответ?"
                    s "Наверное это...{w}x v y?"
                    o_v "Хм, у меня я смотрю ответ другой получился"
                    o_v "Где-то ты ошибку допустил, давай смотреть"
                    window hide
                    pause
                    pause
                    window show
                    o_v "..."
                    o_v "А, ну конечно ты же скобку неверно раскрыл во второй строке"
                    s "..."
                    o_v "Кто-нибудь подскажет как тут нужно поступить?"
                    g "Я знаю! Тут будет вот так"
                    o_v "Отлично..."
                    g "Георгий, можно просто - Гоша"
                    o_v "Гоша молодец!"
                    o_v "Ты понял..."
                    s "Станислав, можно просто - Стас"
                    o_v "...Стас?"
                    s "Да, мне просто нужно подучить таблицу с формулами"
                    o_v "Хорошо"
                    o_v "Итак, у кого-нибудь еще остались вопросы?"
                    stud "..."
                    o_v "Тогда продолжаем..."
                    o_v "Присаживайся"
                    "~ Черт, я допустил ошибку, а ведь это еще легкий пример... ~"
                    "~ Ладно, в любом случае это был интересный опыт ~"
            stop music fadeout(5.0)   
        "Воздержаться":
            $ uspevaemost -= 1
            "~ Не думаю, что это хорошая идея ~"
            "~ Лучше предоставлю это дело профессионалам ~"
            o_v "Так-так...О!"
            o_v "Вот парень в белой рубашке выходи"
            g "Я?"
            o_v "Нет, моя бабушка!"
            stud "Ахахаха"
            g "У нас преобразования?"
            o_v "Да упростить с помощью элементарных преобразований"
            window hide
            pause
            pause
            window show
            o_v "Так ну и какой же ответ?"
            g "У меня выходит x"
            o_v "У меня тоже, молодец, присаживайся"
            o_v "Вот так чтобы все решали, четко{w}, быстро{w}, а главное - точно"
            o_v "У кого-нибудь есть вопросы?"
            stud "..."
    o_v "Поднимаем ставки...следующий пример"
    window hide
    pause
    pause
    window show
    play sound "sounds/dgtu_zvon.mp3"
    o_v "Так, на сегодня хватит, все свободны, домашнее задание я вам дала"
    stud "Спасибо! До свидания!"
    jump D1T2



