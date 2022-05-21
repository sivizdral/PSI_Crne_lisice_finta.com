$(document).ready(function() {

    inicijalizacija()

    function inicijalizacija() {
        inicijalizujTeren()
    }

    function inicijalizujTeren() {
        $(".position").css("background-color", "red").hide()
        $(".primary").show()
    }


})