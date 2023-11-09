document.addEventListener('DOMContentLoaded', function() {
    console.log('Script loaded!');

    // Add some interactivity
    var resultElement = document.getElementById('result');
    if (resultElement) {
        resultElement.addEventListener('click', function() {
            alert('You clicked the result!');
        });
    }
});
