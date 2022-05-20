// For Filters
document.addEventListener("DOMContentLoaded", function() {
    var filterBtn = document.getElementById('filter-btn');
    var btnTxt = document.getElementById('btn-txt');
    var filterAngle = document.getElementById('filter-angle');

    $('#filterbar').collapse(false);
    var count = 0, count2 = 0;
    function changeBtnTxt() {
    $('#filterbar').collapse(true);
    count++;
    if (count % 2 != 0) {
    filterAngle.classList.add("fa-angle-right");
    btnTxt.innerText = "show filters"
    filterBtn.style.backgroundColor = "#36a31b";
    }
    else {
    filterAngle.classList.remove("fa-angle-right")
    btnTxt.innerText = "hide filters"
    filterBtn.style.backgroundColor = "#ff935d";
    }

    }

    // For Applying Filters
    $('#inner-box').collapse(false);
    $('#inner-box2').collapse(false);

    // For changing NavBar-Toggler-Icon
    var icon = document.getElementById('icon');

    function chnageIcon() {
    count2++;
    if (count2 % 2 != 0) {
    icon.innerText = "";
    icon.innerHTML = '<span class="far fa-times-circle" style="width:100%"></span>';
    icon.style.paddingTop = "5px";
    icon.style.paddingBottom = "5px";
    icon.style.fontSize = "1.8rem";


    }
    else {
    icon.innerText = "";
    icon.innerHTML = '<span class="navbar-toggler-icon"></span>';
    icon.style.paddingTop = "5px";
    icon.style.paddingBottom = "5px";
    icon.style.fontSize = "1.2rem";
    }
    }

    // Showing tooltip for AVAILABLE COLORS
    $(function () {
    $('[data-tooltip="tooltip"]').tooltip()
    })

    // For Range Sliders
    var inputLeft = document.getElementById("input-left");
    var inputRight = document.getElementById("input-right");

    var thumbLeft = document.querySelector(".slider > .thumb.left");
    var thumbRight = document.querySelector(".slider > .thumb.right");
    var range = document.querySelector(".slider > .range");

    var amountLeft = document.getElementById('amount-left')
    var amountRight = document.getElementById('amount-right')

    function setLeftValue() {
    var _this = inputLeft,
    min = parseInt(_this.min),
    max = parseInt(_this.max);

    _this.value = Math.min(parseInt(_this.value), parseInt(inputRight.value) - 1);

    var percent = ((_this.value - min) / (max - min)) * 100;

    thumbLeft.style.left = percent + "%";
    range.style.left = percent + "%";
    amountLeft.innerText = parseInt(percent * 10);
    }
    setLeftValue();

    function setRightValue() {
    var _this = inputRight,
    min = parseInt(_this.min),
    max = parseInt(_this.max);

    _this.value = Math.max(parseInt(_this.value), parseInt(inputLeft.value) + 1);

    var percent = ((_this.value - min) / (max - min)) * 100;

    amountRight.innerText = parseInt(percent * 10);
    thumbRight.style.right = (100 - percent) + "%";
    range.style.right = (100 - percent) + "%";
    }
    setRightValue();

    inputLeft.addEventListener("input", setLeftValue);
    inputRight.addEventListener("input", setRightValue);

    inputLeft.addEventListener("mouseover", function () {
    thumbLeft.classList.add("hover");
    });
    inputLeft.addEventListener("mouseout", function () {
    thumbLeft.classList.remove("hover");
    });
    inputLeft.addEventListener("mousedown", function () {
    thumbLeft.classList.add("active");
    });
    inputLeft.addEventListener("mouseup", function () {
    thumbLeft.classList.remove("active");
    });

    inputRight.addEventListener("mouseover", function () {
    thumbRight.classList.add("hover");
    });
    inputRight.addEventListener("mouseout", function () {
    thumbRight.classList.remove("hover");
    });
    inputRight.addEventListener("mousedown", function () {
    thumbRight.classList.add("active");
    });
    inputRight.addEventListener("mouseup", function () {
    thumbRight.classList.remove("active");
    });
    });

      /*$(document).ready(function() {
        $('.buy').click(function(){
          $('.bottom').addClass("clicked");
        });

        $('.remove').click(function(){
          $('.bottom').removeClass("clicked");
        });
        });*/

let currentPage = 1;
let numberOfCards = 0;

function setPageClasses(text) {
  let number = currentPage % 3;
  if (number == 1) $('#firstitem').removeClass("active");
  else if (number == 2) $('#seconditem').removeClass("active");
  else if (number == 0) $('#thirditem').removeClass("active");
  let newnumber = parseInt(text) % 3;
  if (newnumber == 1) $('#firstitem').addClass("active");
  else if (newnumber == 2) $('#seconditem').addClass("active");
  else if (newnumber == 0) $('#thirditem').addClass("active");
}

function getFirstPage() {
  let text = document.getElementById("first-page").innerText;
  setPageClasses(text);
  currentPage = parseInt(text);
  changeProducts();
}

function getSecondPage() {
  let text = document.getElementById("second-page").innerText;
  setPageClasses(text);
  currentPage = parseInt(text);
  changeProducts();
}

function getThirdPage() {
  let text = document.getElementById("third-page").innerText;
  setPageClasses(text);
  currentPage = parseInt(text);
  changeProducts();
}

function nextPage() {
    let number = currentPage % 3;
    if (number == 0) {
        let text = document.getElementById("first-page").innerText;
        let pageNum = parseInt(text);
        if (numberOfCards / 3 > (pageNum + 2)) {
            document.getElementById("first-page").textContent = parseInt(text) + 3;
            document.getElementById("second-page").textContent = parseInt(text) + 4;
            document.getElementById("third-page").textContent = parseInt(text) + 5;
            if (numberOfCards / 3 < (pageNum + 4)) document.getElementById("second-page").style.display = "none";
            if (numberOfCards / 3 < (pageNum + 5)) document.getElementById("third-page").style.display = "none";
            getFirstPage();
        }

    } else if (number == 1) {
        getSecondPage();
    } else getThirdPage();

}

function prevPage() {
    let number = currentPage % 3;
    if (number == 1) {
        let text = document.getElementById("first-page").innerText;
        let pageNum = parseInt(text);
        if (pageNum > 1) {
            document.getElementById("first-page").textContent = parseInt(text) - 3;
            document.getElementById("second-page").textContent = parseInt(text) - 2;
            document.getElementById("third-page").textContent = parseInt(text) - 1;
            if (document.getElementById("second-page").style.display === "none") document.getElementById("second-page").style.display = "block";
            if (document.getElementById("third-page").style.display === "none") document.getElementById("third-page").style.display = "block";
            getThirdPage();
        }
    } else if (number == 0) {
        getSecondPage();
    } else getFirstPage();

}

let filtered = []
let appliedFilter = false;

function resetFilters() {
    filtered = document.getElementsByClassName("wrapperrr");
    let box = document.getElementById("inner-box");
    let leagueCount = box.childElementCount;
    for(let i = 1; i <= leagueCount; i++) {
        let id = "leagueSelector" + i;
        document.getElementById(id).checked = false;
        let elem = document.getElementById("filter" + id);
        if (elem != null) document.getElementById("price").removeChild(elem);
    }
    let box2 = document.getElementById("inner-box2");
    let typeCount = box2.childElementCount;
    for(let i = 1; i <= typeCount; i++) {
        let id = "typeSelector" + i;
        document.getElementById(id).checked = false;
        let elem = document.getElementById("filter" + id);
        if (elem != null) document.getElementById("price").removeChild(elem);
    }
    refreshProducts();
    currentPage = 1;
    changeProducts();
    appliedFilter = false;
}


function applyFilters() {
    //document.getElementById("filterform").submit();
    let appliedLeagues = ['']
    let appliedTypes = []
    let lowPrice = 0
    let highPrice = 1000
    let box = document.getElementById("inner-box");
    let leagueCount = box.childElementCount;
    for(let i = 1; i <= leagueCount; i++) {
        let id = "leagueSelector" + i;
        if (document.getElementById(id).checked) {
            let nameid = id.replace('Selector','Name');
            appliedLeagues.push(document.getElementById(nameid).innerText);
        }
    }
    let box2 = document.getElementById("inner-box2");
    let typeCount = box2.childElementCount;
    for(let i = 1; i <= typeCount; i++) {
        let id = "typeSelector" + i;
        if (document.getElementById(id).checked) {
            let nameid = id.replace('Selector','Name');
            appliedTypes.push(document.getElementById(nameid).innerText);
        }
    }
    var amountLeft = document.getElementById('amount-left');
    var amountRight = document.getElementById('amount-right');
    lowPrice = amountLeft.innerText;
    highPrice = amountRight.innerText;
    //document.getElementById("tokens").innerText = appliedTypes.length;
    filtered = [];
    cards = document.getElementsByClassName("wrapperrr");
    numberOfCards = cards.length;
    let arr = [];
    for (let i = 0; i < numberOfCards; i++) {
        let index = i+1;
        let league = document.getElementById("productLeague"+index).innerText;
        let type = document.getElementById("productType"+index).innerText;
        let price = document.getElementById("productValue"+index).innerText;
        price = parseInt(price.replace(' tokens',''));
        let p = false, t = false, l = false;
        if (price >= lowPrice && price <= highPrice) {
            p = true;
        }
        if (appliedLeagues.length > 1) {
            if (appliedLeagues.includes(league)) {
                l = true;
            }
        } else l = true;
        if (appliedTypes.length > 0) {
            if (appliedTypes.includes(type)) {
                t = true;
            }
        } else t = true;
        if (l && p && t) {
            filtered.push(cards[i]);
        }
    }
    //document.getElementById("tokens").innerText = filtered.length;
    numberOfCards = filtered.length;
    appliedFilter = true;
    refreshProducts();
    currentPage = 1;
    changeProducts();
}

function refreshProducts() {
    cards = document.getElementsByClassName("wrapperrr");
    number = cards.length;
    for (let i = 0; i < number; i++) {
        if (cards[i] in filtered) {
            cards[i].style.display = "block";
        } else {
            cards[i].style.display = "none";
        }
    }
}

function addFilter(id) {
    /*let checkbox = document.getElementById(id);
    if (checkbox.checked == true) {
        let elem = document.createElement("input");
        elem.type = "hidden";
        elem.id = "filter" + id;
        if (id.includes("type")) {
            elem.name = "typeFilter";
        } else {
            elem.name = "leagueFilter";
        }
        elem.value = id.slice(-1);
        document.getElementById("filterform").appendChild(elem);
    } else {
        let elem = document.getElementById("filter" + id);
        document.getElementById("filterform").removeChild(elem);
    }*/

}

let cards = []

function changeProducts() {
    if (!appliedFilter) filtered = document.getElementsByClassName("wrapperrr");

    //cards = document.getElementsByClassName("wrapper");
    //numberOfCards = cards.length;
    //cards = filtered;
    numberOfCards = filtered.length;
    let first = (currentPage - 1) * 3;
    let last = first + 2;
    for (let i = 0; i < filtered.length; i++) {
        if (i >= first && i <= last) {
            filtered[i].style.display = "block";
        } else {
            filtered[i].style.display = "none";
        }
    }

    //document.getElementById("tokens").innerText = numberOfCards;
}

function hideSubmits() {
    let submits = document.getElementsByClassName('submitProductForm');
    let number = submits.length;
    for (let i = 0; i < number; i++) {
        submits[i].style.display = "none";
    }
    //document.getElementById("submitFilterForm").style.display = "none";
}

let cartProducts = []
let totalCartValue = 0;

function loadPage() {
    changeProducts();
    hideSubmits();
    loadPreviousProducts();
}

window.onload = loadPage;

function loadPreviousProducts() {
    let text = document.getElementById("hiddencartstring").innerText;
    cartProducts = text.split(',');
}

function chosenProduct(id) {
    let elem = document.getElementById(id).parentElement.parentElement;
    elem.classList.add("clicked");
    let value = elem.firstElementChild.firstElementChild.firstElementChild.nextElementSibling.innerHTML;
    value = parseInt(value.replace(' tokens',''));
    totalCartValue += value;
    let formid = id.replace('buy','productForm');
    //document.getElementById(formid).submit();
    let newid = id.replace('buy','');
    cartProducts.push(newid);
    let scitemid = 'scitem' + newid;
    document.getElementById(scitemid).style.display = "block";
    document.getElementById("itemCounter").innerText = "ITEMS: " + (cartProducts.length - 1);
    document.getElementById("totalPriceCounter").innerText = "" + totalCartValue + " tokens";
    document.getElementById("finalPriceCounter").innerText = "" + totalCartValue + " tokens";
}

function removeProduct(id) {
    let elem = document.getElementById(id).parentElement.parentElement;
    let value = elem.firstElementChild.firstElementChild.firstElementChild.nextElementSibling.innerHTML;
    value = parseInt(value.replace(' tokens',''));
    totalCartValue -= value;
    let newid = id.replace('remove','');
    let scitemid = 'scitem' + newid;
    document.getElementById(scitemid).style.display = "none";
    cartProducts.splice(cartProducts.indexOf(newid),1);
    elem.classList.remove("clicked");
    document.getElementById("itemCounter").innerText = "ITEMS: " + (cartProducts.length - 1);
    document.getElementById("totalPriceCounter").innerText = "" + totalCartValue + " tokens";
    document.getElementById("finalPriceCounter").innerText = "" + totalCartValue + " tokens";
}

let clicked = 0;
let finalValue = totalCartValue;

function goToCart(id) {
    finalValue = totalCartValue;
    if (!clicked) {
        cards = document.getElementsByClassName("wrapperrr");
        number = cards.length;
        for (let i = 0; i < number; i++) {
                cards[i].style.display = "none";
        }
        document.getElementById("shoppingcart").style.display = "block";
        document.getElementById("cartinput").value = cartProducts.join();
        document.getElementById(id).innerText = "BACK TO SHOP";
        //document.getElementById("cartform").submit();
        clicked = 1;
    } else {
        changeProducts();
        document.getElementById("shoppingcart").style.display = "none";
        document.getElementById(id).innerText = "GO TO CART";
        clicked = 0;
    }

}



function inputCode(id) {
    let codeElem = document.getElementById(id);
    let discountCode = codeElem.innerText;
    finalValue = totalCartValue;
    if (discountCode == "ogrizovic") {
        finalValue = totalCartValue * 0.8;
    } else if (discountCode == "dp") {
        finalValue = totalCartValue * 0.7;
    } else if (discountCode == "tasha") {
        finalValue = totalCartValue * 0.6;
    } else if (discountCode == "drazen") {
        finalValue = totalCartValue * 0.0;
    } else if (discountCode == "bojic") {
        finalValue = totalCartValue * 1.5;
    }
    document.getElementById("finalPriceCounter").innerText = "" + finalValue + " tokens";
}

function checkout() {
    let tokens = parseInt(document.getElementById("tokens").innerText.replace("Available tokens: ",""));
    if (finalValue > tokens) {
        document.getElementById("nocash").style.display = "block";
    } else {
        document.getElementById("nocash").style.display = "none";
        document.getElementById("checkoutform").submit();
    }
}



