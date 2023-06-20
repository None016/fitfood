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

function dobb(asdf){
    window.location.href = asdf;
}

function order(dat){
    document.getElementById("form").submit();

}