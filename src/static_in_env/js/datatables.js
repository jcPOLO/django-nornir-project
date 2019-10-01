apiVersion = 'v1'



/* Formatting function for row details - modify as you need */
function format(id) {
    // `d` is the original data object for the row
    var div = $('<div/>')
        .addClass('loading')
        .text('Loading...');

    $.ajax({
        url: '../' + apiVersion + '/device/' + id,
        dataType: 'json',
        success: function (json) {
            div
                .html(showTableDetails(json))
                .removeClass('loading');
        },
        error: function (error_data) {
            console.log("error in ajax request")
        }
    });

    return div;
}


function showTableDetails(d) {
    return '<table cellpadding="5" cellspacing="0" border="0" style="padding-left:50px;">' +
        '<tr>' +
        '<td>Serial:</td>' +
        '<td>' + d.serial + '</td>' +
        '</tr>' +
        '</table>';
}


$(document).ready(function () {

    // Add event listener for opening and closing details
    $('#devices_table tbody').on('click', 'td.details-control', function () {
        var tr = $(this).closest('tr');
        var id = tr.children('td').attr('id')
        var row = table.row(tr);

        if (row.child.isShown()) {
            // This row is already open - close it
            row.child.hide();
            tr.removeClass('shown');
        }
        else {
            // Open this row
            row.child(format(id)).show();
            tr.addClass('shown');
        }
    });

    var table = $('#devices_table').DataTable({
        dom: 'B<"clear">lfrtip',
        buttons: {
            name: 'primary',
            buttons: ['copy', 'csv', 'excel', 'pdf']
        }
    });



    $('#devices_table tbody').on('click', 'tr', function () {
        $(this).toggleClass('selected');
    });

    $('#button').click(function () {
        alert(table.rows('.selected').data().length + ' row(s) selected');
    });

});
