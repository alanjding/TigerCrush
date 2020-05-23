// Author: Alan Ding

function isInputEmpty() {
    return $('#crushSelector').val() === '';
}

$('#addCrushButton').click(function() {
    if (isInputEmpty()) {
        $('#crushSelector').addClass('is-invalid');
    }
    else {
        $('#confirmModal').modal('show');
    }
});

$('#submitButton').click(function() {
    if (!isInputEmpty())
        $('#addCrushForm').submit();
});