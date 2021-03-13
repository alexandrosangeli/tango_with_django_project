$(document).ready(function () {
    $("#about-btn").click(function(){
        alert("You clicked the button using jQuery!")
    });

    $('p').hover(
        function(){
            $(this).css('color','red')
        },
        function(){
            $(this).css('color','black')
        }
    );

    $('#about-btn').click(function() {
        msgStr = $('#msg').html();
        msgStr += ' ooo, fancy!';

        $('#msg').html(msgStr);
    });
});

