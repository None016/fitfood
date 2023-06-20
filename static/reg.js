function reg()
{
    var h = '<!DOCTYPE html><html lang="en"><head> <meta charset="UTF-8"> <meta http-equiv="X-UA-Compatible" content="IE=edge"> <meta name="viewport" content="width=device-width, initial-scale=1.0"> <link rel="stylesheet" href="reg.css"> <title>Document</title></head><body> <header> <img class="logo" src="Logo.png"> <h2 class="fitfood">FitFood</h2> <div class="menu"> <a href="#">Главная</a> <a href="#">Меню</a> <a href="#">Корзина</a> <a href="#">Контакты</a> <a href="#">Вход</a> </div> </header> <article> <h2>Регистрация</h2> <form class="forma" action="" method="post"> <h3>*Никнейм</h3> <input type="text"> <h3>*Номер телефона</h3> <input type="tel"> <h3>Адрес</h3> <input type="text"> <h3>*Пороль</h3> <input type="password"> <h3>*Пароль повтор</h3> <input type="password"> </form> <button class = "vhod">Вход</button> <div class="boto"> <a href="#">Регистрация через Telegram</a> <a onclick="vhod()" href="#">Вход</a> </div> </article> <script src = "reg.js"></script></body></html>';
    document.write(h);
    document.close();
}

function vhod()
{
    document.write('<!DOCTYPE html><html lang="en"><head> <meta charset="UTF-8"> <meta http-equiv="X-UA-Compatible" content="IE=edge"> <meta name="viewport" content="width=device-width, initial-scale=1.0"> <link rel="stylesheet" href="reg.css"> <title>Document</title></head><body> <header> <img class="logo" src="Logo.png"> <h2 class="fitfood">FitFood</h2> <div class="menu"> <a href="#">Главная</a> <a href="#">Меню</a> <a href="#">Корзина</a> <a href="#">Контакты</a> <a href="#">Вход</a> </div> </header> <article> <h2>Вход</h2> <form class="forma" action="" method="post"> <h3>Никнейм</h3> <input type="text"> <h3>Пароль</h3> <input type="password"> </form> <button class = "vhod">Вход</button> <div class="boto"> <a href="#">Забыл пороль</a> <a onclick="reg()" href="#">Регистрация</a> </div> </article> <script src = "reg.js"></script></body></html>');
    document.close();
}

function submit()
{
    document.getElementById("form").submit();
}