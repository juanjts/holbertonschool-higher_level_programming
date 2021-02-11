$(document).ready(function () {
  $.getJSON('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
    for (const x of data.results) {
      $('UL#list_movies').append('<li>' + x.title + '</li>');
    }
  });
});
