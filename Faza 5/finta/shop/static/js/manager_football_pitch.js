$(document).ready(function() {

    previous_item = ""
    previous_item_id = ""

    inicijalizacija()

    function inicijalizacija() {
        inicijalizujTeren()
        dodajDogadjaje()
        ostalo()
    }

    function ostalo() {
        $("#position_name").html("(Select a position in order to search for a player)").css("color", "red")
        $("#player_search").attr("disabled", true)
    }

    function dodajDogadjaje() {
        $(".position").on({click: function() {
            pretraziIgraca($(this))
        }})
        $("#player").on({change: function() {
            if (previous_item_id !== "" && $(this).val().length >= 4 && $("#player_team").val().length >= 4) {
                $("#player_search").attr("disabled", false)
            }
            else {
                $("#player_search").attr("disabled", true)
            }
        }})
        $("#player_team").on({change: function() {
            if (previous_item_id !== "" && $(this).val().length >= 4 && $("#player").val().length >= 4) {
                $("#player_search").attr("disabled", false)
            }
            else {
                $("#player_search").attr("disabled", true)
            }
        }})
    }

    function inicijalizujTeren() {
        $(".position").css("background-color", "red").hide()
        $(".primary").show()
    }

    function pretraziIgraca(item) {
        if (item.attr("id") === previous_item_id) {
            item.css("background-color", "red")
            previous_item = ""
            previous_item_id = ""
            $("#position_name").html("(Select a position in order to search for a player)").css("color", "red")
            $("#player_search").attr("disabled", true)
        }
        else {
            if (previous_item_id !== "") {
                previous_item.css("background-color", "red")
            }

            previous_item = item
            previous_item_id = item.attr("id")
            $("#position_name").html("Search for a player at " + previous_item_id +
                " position (team and player names, at least 4 letters each, no spaces):").css("color", "black")
            if ($("#player").val().length >= 4 && $("#player_team").val().length >= 4) {
                $("#player_search").attr("disabled", false)
            }

            item.css("background-color", "black")
        }
    }


})

function dodajIgraca() {
    alert("oh my")
}