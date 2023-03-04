// Function to show each Collection from dropdown menu
function dropdownview(name)
{
    if(name == "")
        return;

    var collection = new XMLHttpRequest();

    collection.onreadystatechange = function() {
        if (collection.readyState == 4 && collection.status == 200) {
            // do something to the page
            $('#infodiv').html(collection.responseText);
        }
    };
    collection.open('GET', "static/" + name + '.html', true);
    collection.send();
};


// function to add items to shopping cart and send to python
let cartbutton = document.getElementsByName('ropebutton');
console.log(cartbutton) // prints node []
qty = 0;
for(var i = 0; i < cartbutton.length; i++) {
    let button = cartbutton[i];
    button.addEventListener('click', (event) => {
        ++qty;
        document.getElementById('cart1').innerHTML = qty;
        console.clear();
        console.log(event.target);
        console.log(event.target.dataset.test);
        const s = JSON.stringify(event.target.dataset.test)
        console.log(s)
        $.ajax({
            url:"/test",
            type:"POST",
            contentType: "application/json",
            data: JSON.stringify(s)});
    });   
};


// when button pressed display 'qty + added to cart' for 2 seconds
var aa = 0;
function button111Click() {
    text = ++aa + " added to cart"
    document.getElementById('rope111').innerHTML = text;
    setTimeout(function(){
        document.getElementById('rope111').innerHTML = rope111.value;
    }, 2000);
}

// when button pressed display 'qty + added to cart'
var ab = 0;
function button112Click() {
    text = ++ab + " added to cart"
    document.getElementById('rope112').innerHTML = text;
    setTimeout(function(){
        document.getElementById('rope112').innerHTML = rope112.value;
    }, 2000);
}


// when button pressed display 'qty + added to cart'
var ac = 0;
function button113Click() {
    text = ++ac + " added to cart"
    document.getElementById('rope113').innerHTML = text;
    setTimeout(function(){
        document.getElementById('rope113').innerHTML = rope113.value;
    }, 2000);
}

// when button pressed display 'qty + added to cart'
var ad = 0;
function button114Click() {
    text = ++ad + " added to cart"
    document.getElementById('rope114').innerHTML = text;
    setTimeout(function(){
        document.getElementById('rope114').innerHTML = rope114.value;
    }, 2000);
}

// when button pressed display 'qty + added to cart'
var ae = 0;
function button115Click() {
    text = ++ae + " added to cart"
    document.getElementById('rope115').innerHTML = text;
    setTimeout(function(){
        document.getElementById('rope115').innerHTML = rope115.value;
    }, 2000);
}

// when button pressed display 'qty + added to cart'
var af = 0;
function button116Click() {
    text = ++af + " added to cart"
    document.getElementById('rope116').innerHTML = text;
    setTimeout(function(){
        document.getElementById('rope116').innerHTML = rope116.value;
    }, 2000);
}

// when button pressed display 'qty + added to cart'
var ag = 0;
function button117Click() {
    text = ++ag + " added to cart"
    document.getElementById('rope117').innerHTML = text;
    setTimeout(function(){
        document.getElementById('rope117').innerHTML = rope117.value;
    }, 2000);
}

// when button pressed display 'qty + added to cart'
var ah = 0;
function button118Click() {
    text = ++ah + " added to cart"
    document.getElementById('rope118').innerHTML = text;
    setTimeout(function(){
        document.getElementById('rope118').innerHTML = rope118.value;
    }, 2000);
}

// when button pressed display 'qty + added to cart'
var ai = 0;
function button119Click() {
    text = ++ai + " added to cart"
    document.getElementById('rope119').innerHTML = text;
    setTimeout(function(){
        document.getElementById('rope119').innerHTML = rope119.value;
    }, 2000);
}

// when button pressed display 'qty + added to cart'
var aj = 0;
function button121Click() {
    text = ++aj + " added to cart"
    document.getElementById('city121').innerHTML = text;
    setTimeout(function(){
        document.getElementById('city121').innerHTML = city121.value;
    }, 2000);
}

// when button pressed display 'qty + added to cart'
var ak = 0;
function button122Click() {
    text = ++ak + " added to cart"
    document.getElementById('city122').innerHTML = text;
    setTimeout(function(){
        document.getElementById('city122').innerHTML = city122.value;
    }, 2000);
}

// when button pressed display 'qty + added to cart'
var al = 0;
function button123Click() {
    text = ++al + " added to cart"
    document.getElementById('city123').innerHTML = text;
    setTimeout(function(){
        document.getElementById('city123').innerHTML = city123.value;
    }, 2000);
}

// when button pressed display 'qty + added to cart'
var am = 0;
function button124Click() {
    text = ++am + " added to cart"
    document.getElementById('city124').innerHTML = text;
    setTimeout(function(){
        document.getElementById('city124').innerHTML = city124.value;
    }, 2000);
}

// when button pressed display 'qty + added to cart'
var an = 0;
function button125Click() {
    text = ++an + " added to cart"
    document.getElementById('city125').innerHTML = text;
    setTimeout(function(){
        document.getElementById('city125').innerHTML = city125.value;
    }, 2000);
}

// when button pressed display 'qty + added to cart'
var ao = 0;
function button126Click() {
    text = ++ao + " added to cart"
    document.getElementById('city126').innerHTML = text;
    setTimeout(function(){
        document.getElementById('city126').innerHTML = city126.value;
    }, 2000);
}

// when button pressed display 'qty + added to cart'
var ap = 0;
function button127Click() {
    text = ++ap + " added to cart"
    document.getElementById('city127').innerHTML = text;
    setTimeout(function(){
        document.getElementById('city127').innerHTML = city127.value;
    }, 2000);
}

// when button pressed display 'qty + added to cart'
var aq = 0;
function button128Click() {
    text = ++aq + " added to cart"
    document.getElementById('city128').innerHTML = text;
    setTimeout(function(){
        document.getElementById('city128').innerHTML = city128.value;
    }, 2000);
}

// when button pressed display 'qty + added to cart'
var ar = 0;
function button129Click() {
    text = ++ar + " added to cart"
    document.getElementById('city129').innerHTML = text;
    setTimeout(function(){
        document.getElementById('city129').innerHTML = city129.value;
    }, 2000);
}

// when button pressed display 'qty + added to cart'
var as = 0;
function button131Click() {
    text = ++as + " added to cart"
    document.getElementById('graf131').innerHTML = text;
    setTimeout(function(){
        document.getElementById('graf131').innerHTML = graf131.value;
    }, 2000);
}

// when button pressed display 'qty + added to cart'
var at = 0;
function button132Click() {
    text = ++at + " added to cart"
    document.getElementById('graf132').innerHTML = text;
    setTimeout(function(){
        document.getElementById('graf132').innerHTML = graf132.value;
    }, 2000);
}

// when button pressed display 'qty + added to cart'
var au = 0;
function button133Click() {
    text = ++au + " added to cart"
    document.getElementById('graf133').innerHTML = text;
    setTimeout(function(){
        document.getElementById('graf133').innerHTML = graf133.value;
    }, 2000);
}

// when button pressed display 'qty + added to cart'
var av = 0;
function button134Click() {
    text = ++av + " added to cart"
    document.getElementById('graf134').innerHTML = text;
    setTimeout(function(){
        document.getElementById('graf134').innerHTML = graf134.value;
    }, 2000);
}

// when button pressed display 'qty + added to cart'
var aw = 0;
function button135Click() {
    text = ++aw + " added to cart"
    document.getElementById('graf135').innerHTML = text;
    setTimeout(function(){
        document.getElementById('graf135').innerHTML = graf135.value;
    }, 2000);
}

// when button pressed display 'qty + added to cart'
var ax = 0;
function button136Click() {
    text = ++ax + " added to cart"
    document.getElementById('graf136').innerHTML = text;
    setTimeout(function(){
        document.getElementById('graf136').innerHTML = graf136.value;
    }, 2000);
}

// when button pressed display 'qty + added to cart'
var ay = 0;
function button137Click() {
    text = ++ay + " added to cart"
    document.getElementById('graf137').innerHTML = text;
    setTimeout(function(){
        document.getElementById('graf137').innerHTML = graf137.value;
    }, 2000);
}

// when button pressed display 'qty + added to cart'
var az = 0;
function button138Click() {
    text = ++az + " added to cart"
    document.getElementById('graf138').innerHTML = text;
    setTimeout(function(){
        document.getElementById('graf138').innerHTML = graf138.value;
    }, 2000);
}

// when button pressed display 'qty + added to cart'
var aaa = 0;
function button139Click() {
    text = ++aaa + " added to cart"
    document.getElementById('graf139').innerHTML = text;
    setTimeout(function(){
        document.getElementById('graf139').innerHTML = graf139.value;
    }, 2000);
}


