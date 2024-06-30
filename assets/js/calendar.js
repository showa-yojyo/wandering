document.addEventListener("DOMContentLoaded", initCalendar);

function initCalendar(event){
    const dateControl = document.querySelector('input[id="start"]');
    dateControl.min = '2018-06-01';
    dateControl.max = '2020-04-27';
    dateControl.value = dateControl.max;
}

function navigateToDiaryPage(basePath){
    const dateControl = document.querySelector('input[id="start"]');
    const date = dateControl.value.replaceAll('-', '/'); // "YYYY/mm/dd"
    const url = `${basePath}/diary/${date}/diary.html`
    console.debug(url);
    window.location.href = encodeURI(url);
}
