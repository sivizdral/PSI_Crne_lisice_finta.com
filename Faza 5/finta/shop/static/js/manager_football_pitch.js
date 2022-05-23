$(document).ready(function() {

    inicijalizacija()

    function inicijalizacija() {
        inicijalizujTeren()
        inicijalizujOstalo()
    }

    function inicijalizujTeren() {
        $(".position").css("background-color", "red").hide()
        $(".primary").show()
    }

    function inicijalizujOstalo() {
    }

})