const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
const base_url = '/api/';
const form = document.getElementById('url-form');
const resultSection = document.querySelector(".result-section");
const clearBtn = document.querySelector('.clear-btn');
const showDetails = document.querySelector('#show-details');
const info = document.querySelector('.info')

form.addEventListener('submit', handleForm);

function handleForm(e) {

    e.preventDefault();
    const link = document.querySelectorAll('input')[1].value;
    let objToPost = {"url": `${link}`}
    document.querySelectorAll('input')[1].value = '';

    if (resultSection.innerHTML === '' || resultSection.innerHTML === `<h1 id="error-message">Something Went Wrong.Try with Another URL</h1>` ){
        resultSection.innerHTML = 'Thinking...';
    }

    fetch(base_url, {
        'method': 'POST',
        headers: {'X-CSRFToken': csrftoken, "Content-Type": "application/json"},
        body: JSON.stringify(objToPost)
    })
        .then(res => res.json())
        .then((data) => resultSection.innerHTML = createElementWithResult(data))
        .catch((err) =>{

             resultSection.innerHTML = `<h1 id="error-message">Something Went Wrong.Try with Another URL</h1>`
            // setTimeout(() => {resultSection.innerHTML = ''}, 2000 )
        }

        )

}


function createElementWithResult(d) {
    
    let splitted = d['prediction1'].split(' ');
    let firstPredictionPercentage = splitted[5]
    if (Number(firstPredictionPercentage) < 10){
        return `<h1 id="error-message">No Dog in the Picture or I've Never Seen This One Before</h1>`}
    
    if (d['prediction1'] && d['url'] && d['prediction2'] && d['prediction3']) {
        let template = `<article class="result-wrapper">
                        <img src="${d['url']}" alt="">
                        <ul>
                            <li>${d['prediction1']}</li>
                            <li>${d['prediction2']}</li>
                            <li>${d['prediction3']}</li>
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
