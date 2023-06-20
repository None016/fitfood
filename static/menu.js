function open1(post, post2){        
    document.getElementById(post2).style = 'transform: scale(1);';
    document.getElementById(post).style = 'overflow-y: scroll; z-index: 2; transform: scale(1);';
    document.getElementById('docc').style = 'overflow-y: hidden;';
}    

function clous1(post, post2){   
    document.getElementById(post).style = 'transform: scale(0); z-index: none; transform: scale(0);';
    document.getElementById(post2).style = 'overflow-y: none;';
    document.getElementById('docc').style = 'overflow-y: scroll;';
}  


function dobb(id1, id2){
    $.ajax({
      type:'POST',
      url:'/menu',
      data:{
        todo: id1
      },
    })
    document.getElementById(id2).style = 'background-color: #ffffff; color: #000;';
    document.getElementById(id2).innerHTML = 'Добавлено';
}

function ubr(){
    document.getElementById('pop').style = 'transform: scale(0); z-index: none; transform: scale(0);';
}

function dobav(){
    document.getElementById('pop').style = 'transform: scale(1); z-index: 100; transform: scale(1);';
}