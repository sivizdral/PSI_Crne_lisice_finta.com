$(document).ready(function() {

    previous_item = ""
    previous_item_id = ""
    manager_team = []
    selected_position = ""

    inicijalizacija()

    function inicijalizacija() {
        inicijalizujLocalStorage()
        inicijalizujTeren()
        dodajDogadjaje()
        ostalo()
    }

    function ostalo() {
        $("#position_name").html("(Select a position in order to search for a player)").css("color", "red")
        $("#player_search").attr("disabled", true)

        if (selected_position !== "") {
            $("#" + selected_position).css("background-color", "black")
        }
    }

    function inicijalizujLocalStorage() {
        if (localStorage.getItem("team") == null) localStorage.setItem("team", manager_team)
        else manager_team = localStorage.getItem("team")
        if (localStorage.getItem("selected_position") == null) localStorage.setItem("selected_position", selected_position)
        else selected_position = localStorage.getItem("selected_position")
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
        $("#player_search").on({change: function() {
            console.log("oh my")
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
            localStorage.setItem("selected_position", "")
        }
        else {
            if (previous_item_id !== "") {
                previous_item.css("background-color", "red")
            }

            previous_item = item
            previous_item_id = item.attr("id")
            localStorage.setItem("selected_position", previous_item_id)

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