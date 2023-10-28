label D1AS_CHILL:
    scene CHILL
    with fade
    play music "music/Normal_Day.mp3"
    show GOGA_OUTSIDE at center
    show BORYA_OUTSIDE at right
    show DIVAN_SMILE at left
    with dissolve
    d "Так, а теперь я точно курить всем пока"
    hide GOGA_OUTSIDE
    show ZHENYA_OUTSIDE
    with dissolve
    z "Эй, подожди, я ведь даже с новеньким не познакомился"
    "~ Ах, да это же он вместе с Ваней на матлогику опоздал ~"
    "~ Видимо они хорошо дружат раз даже опаздывают вместе ~"
    z "Привет, меня зовут Женя"
    s "Меня зовут Стас, приятно познакомиться"
    z "..."
    s "..."
    d "Ну тогда мы пойдем, всем удачи и не болейте!"
    g "Пока"
    s "Давайте, удачи"
    b "Увидимся"
    hide ZHENYA_OUTSIDE
    hide DIVAN_SMILE
    with dissolve
    b "Так, ну в общем раз уж пары закончились, то я в общагу"
    show GOGA_OUTSIDE at center
    with dissolve
    g "Слушай, Стас а ты тут квартиру снимаешь или в общаге?"
    s "Я из 10 общаги"
    b "Повтори"
    s "Что?..."
    b "Повтори то, что ты сейчас сказал"
    s "А...я из 10 общаги"
    b "Сосед!"
    "Боря обнял Стаса"
    s "Воу-воу полегче Боря ты мне ребра все переломаешь!"
    g "Ахахаха"
    g "Теперь не только одногруппники, а оказывается еще и соседи"
    b "Круто, можно будет друг к другу в гости ходить, я тебе могу на гитаре сыграть"
    s "Буду ждать с нетерпением!"
    g "Ладно, соседи, я пойду, пока мою машину эвакуатор не забрал"
    "~ Он уже водит? Неплохо, я думал следующим летом пойти ~"
    b "Опять припарковался через пятую точку?"
    g "Ну что поделаешь понедельник - день тяжелый"
    b "И не говори"
    g "Все побежал я давайте"
    s "Пока Гоша"
    b "Давай топай уже"
    hide GOGA_OUTSIDE
    show BORYA_OUTSIDE at center
    with move
    b "Нам тоже пора. Нечего тут стоять"
    b "Идем в общагу, или сначала к Ване и Жене на апельсин заскочим?"
    menu:
        "Пойти на апельсин":
            $sociofob -= 1
            s "Давай сначала на апельсин"
            b "Окей. Погнали"
            stop music fadeout(0.5)
            jump D1AS_APELSIN

        "Пойти сразу в общагу":
            s "Слушай, давай лучше сразу в общагу. Что то я устал за сегодня..."
            b "Окей. Погнали"
            stop music fadeout(1.0)
            jump D1AS_OBSHAGA
    
label D1AS_APELSIN:
    scene APELSIN
    with dissolve
    play bgs "sounds/zvuki-na-ulice-goroda.mp3"
    "Стас и Боря пришли на апельсин"
    return

label D1AS_OBSHAGA:
    scene OBSHAGA_VHOD
    show BORYA_OUTSIDE at center
    with dissolve
    play bgs "sounds/zvuki-na-ulice-goroda.mp3"
    b "Так. Ну мы на месте."
    b "Тут наши пути расходятся. {w}Я в пятерочку пойду"
    s "Хорошо. Давай, пока"
    hide BORYA_OUTSIDE with dissolve
    "~ Хм... Славные все же парни {w}этот ВПР24 ~"
    return
    # Тут они потом короче пойдут в общагу и там попрощаются после чего Стас будет играть в игры на ноуте и вечером начнет думать о сегодняшнем дне и тут начнутся рефлексии
