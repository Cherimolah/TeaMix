function print_response(response) {
    let field = document.getElementById("field")
    field.innerHTML = ""
    const game = JSON.parse(response)
    for (let i1 = 0; i1 < game.field.length; ++i1) {
        let row = game.field[i1]
        let row_elem = document.createElement("tr")
        field.appendChild(row_elem)
        for (let i2 = 0; i2 < row.length; ++i2) {
            let element = row[i2]
            let e = document.createElement("td")
            e.style.width = "10%"
            e.style.height = "50px"
            e.style.backgroundImage = "url(/data/tiles/" + (element.number + 1) + ".jpg)"
            row_elem.appendChild(e)
        }
    }
}

function print_response1(response) {
    let field = document.getElementById("field");
    const steps = JSON.parse(response).steps;
    for (let i1 = 0; i1 < steps.length; ++i1) {
        let pair = steps[i1];
        field.rows[pair[0].y].cells[pair[0].x].className = "checked";
        field.rows[pair[1].y].cells[pair[1].x].className = "checked";
    }
}

function httpGetAsync(theUrl, func)
{
    const xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function() { 
        if (xmlHttp.readyState === 4 && xmlHttp.status === 200){
            func(xmlHttp.response)
        }
    }
    xmlHttp.open("GET", theUrl, true); // true for asynchronous 
    xmlHttp.send(null);
}