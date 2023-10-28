$("#id_NS1_10").attr('checked', !$("#NS1_other")[0].disabled);
$("#id_NS1_10").click(function () {
    $("#NS1_other").attr('disabled', !this.checked)
});

$("#id_TFW1_7").attr('checked', !$("#TFW1_other")[0].disabled);
$("#id_TFW1_7").click(function () {
    $("#TFW1_other").attr('disabled', !this.checked)
});