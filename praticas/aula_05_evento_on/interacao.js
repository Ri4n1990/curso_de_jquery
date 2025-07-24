$("#nome").on('focus blur' , ()=>{
    $(".cont").text('Opa! interação com o input')
})

$("#nome").on({

    focus : ()=>{$(".cont").text('input selecionado!')},
    blur : ()=>{$(".cont").text('input não selecionado')}



})




$("#meuform").on('submit', (e)=>{
    
    $('.cont').text('formulario enviado')
})