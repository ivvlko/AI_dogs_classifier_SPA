const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
const base_url = '/api/';
let base_details_url = '/api_details/'
const form = document.getElementById('url-form');
const resultSection = document.querySelector(".result-section");
const clearBtn = document.querySelector('.clear-btn');
const showDetails = document.querySelector('#show-details');
const info = document.querySelector('.info');
const correctBtn = document.getElementById('correct-button');
let hasResult = false;

let currentId = -100;
let currentPrediction = -1

form.addEventListener('submit', handleForm);

correctBtn.addEventListener('click', updateIfResultIsCorrect);


// Making Put Request
function updateIfResultIsCorrect() {
    base_details_url_current = base_details_url + currentId.toString() + '/'
    objToPut = {"correct_prediction": currentPrediction};
    fetch(base_details_url_current, {
        'method': 'PUT',
        headers: {'X-CSRFToken': csrftoken, "Content-Type": "application/json"},
        body: JSON.stringify(objToPut)
    })
    .then(res => res.json())
      .then((data) => {
           correctBtn.innerHTML = 'Thanks!'
           window.setTimeout(() => {
               correctBtn.innerHTML = 'Correct';
               correctBtn.style.display = 'none';
           }, 2000);

        })
}



//Making Post Request
function handleForm(e) {

    e.preventDefault();
    correctBtn.style.display = 'none';
    const link = document.querySelectorAll('input')[1].value;
    let objToPost = {"url": `${link}`}
    document.querySelectorAll('input')[1].value = '';


    if (resultSection.innerHTML === '' || hasResult || resultSection.innerHTML === `<h1 id="error-message">Something Went Wrong.Try with Another URL</h1>` ){
        resultSection.innerHTML = 'Thinking...';
    }

    fetch(base_url, {
        'method': 'POST',
        headers: {'X-CSRFToken': csrftoken, "Content-Type": "application/json"},
        body: JSON.stringify(objToPost)
    })
        .then(res => res.json())
        .then((data) => {
            resultSection.innerHTML = createElementWithResult(data);
            currentId = data['id'];
            currentPrediction = data['predicted_index']
            correctBtn.style.display = 'block';
            hasResult = true;

        })

        .catch((err) =>{

             resultSection.innerHTML = `<h1 id="error-message">Something Went Wrong.Try with Another URL</h1>`
        })

}

// Helping functions below:

function createElementWithResult(d) {

    let splitted = d['prediction1'].split(' ');
    let firstPredictionPercentage = splitted[5]
    if (Number(firstPredictionPercentage) < 10){
        return `<h1 id="error-message">No Dog in the Picture or I've Never Seen This One Before</h1>`}

    if (d['prediction1']) {
        let template = `<article class="result-wrapper">
                        <img src="${d['url']}" alt="">
                        <ul>
                            <li>${d['prediction1']}</li>

                        </ul>
                        </article>`;

        return template;
    } else {
        return `<h1 id="error-message">Something Went Wrong.Try with Another URL</h1>`
    }
}

clearBtn.addEventListener('click', clearContent)

function clearContent() {
    resultSection.innerHTML = '';
    correctBtn.style.display = 'none';
    hasResult = false;
}

showDetails.addEventListener('click', handleDetailsSection)

function handleDetailsSection() {
    if (info.style.display === 'none') {
        info.style.display = 'block';
        showDetails.innerHTML = 'Hide Details';
    } else {
        info.style.display = 'none';
        showDetails.innerHTML = 'Show Details';
    }
}