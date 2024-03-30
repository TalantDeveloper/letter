$(document).ready(function () {

    $('#table .table-tr td:not(:last-child)').click(function () {

        $('#table .inner-tr').slideUp();
        $('#table .table-tr th').click(function () {
            $('.inner-tr').slideUp();
        });

        $(this).parent().next('.inner-tr').slideToggle();

        $(this).parent().next('.inner-tr').css({
            'border': '1px solid rgb(71,130,218)',
            'background-color': 'rgb(71,130,218, 0.2)'
        });

    });


    // order update query	// order update query	// order update query
    // order update query	// order update query	// order update query

    $('#table .table-tr .td-action .fa-edit').click(function () {

    });

    $('#order-group').click(function () {
        $("input").prop('disabled', false);
    });

    $('.abs-box .abs-content .abs-nav #correspond').click(function () {
        $('.abs-box .abs-content .abs-nav .correspond-lists').slideToggle();
    });

    $('.abs-box .abs-content .abs-nav .correspond-list').click(function () {
        $('.abs-box .abs-content .abs-nav #correspond').val($(this).text());
        $('.abs-box .abs-content .abs-nav .correspond-lists').slideUp();
    });
    // order update query	// order update query	// order update query
    // order update query	// order update query	// order update query


    $('#table .table-tr .fa-edit').click(function () {

        $('#table .table-tr').removeClass('bg-blue');
        $(this).parent().parent().addClass('bg-blue');
    });

    // center update query	// center update query	// center update query
    // center update query	// center update query	// center update query

    $('.center #table .table-tr .fa-edit').click(function () {

        $('.center .abs-content .abs-nav .editbtn').css('display', 'block');
        $('.center #center-id-input').val($(this).parent().parent().find('.td-id').text());
        $('.center #center-name-input').val($(this).parent().parent().find('.td-name').text());
        $('.center #center-xodim-input').val($(this).parent().parent().find('.td-xodim').text());
    });

    $('.center .abs-content .abs-nav .editbtn').click(function () {

        $(this).css('display', 'none');

        $('#table .table-tr').removeClass('bg-blue');
        $('.center #center-id-input').val(parseInt($('.center .table-info b').text()) + 1);
        $('.center #center-name-input').val(null);
        $('.center #center-xodim-input').val(null);
    });

    // center update query	// center update query	// center update query
    // center update query	// center update query	// center update query

    // person update query	// person update query	// person update query
    // person update query	// person update query	// person update query

    $('.employe #table .table-tr .fa-edit').click(function () {

        $('.employe .abs-content .abs-nav .editbtn').css('display', 'block');
        $('.employe #employe-id-input').val($(this).parent().parent().find('.td-id').text());
        $('.employe #employe-name-input').val($(this).parent().parent().find('.td-name').text());
    });

    $('.employe .abs-content .abs-nav .editbtn').click(function () {

        $(this).css('display', 'none');

        $('#table .table-tr').removeClass('bg-blue');
        $('.employe #employe-id-input').val(parseInt($('.employe .table-info b').text()) + 1);
        $('.employe #employe-name-input').val(null);
    });

    // person update query	// person update query	// person update query
    // person update query	// person update query	// person update query


    $('.center-page, .dashboard-table').css('height', $(window).height() - ($('.head-bar').height() + 22));
    $('.dashboard .table-info b').text($('.dashboard-table #table tr:last').index() / 2);

    $("#addfile-input").change(function () {

        $('.file-info i').text($(this).val());
        $('.file-info input').slideDown();
    });

    // close abs-content
    $('.abs-box .center .fa-close').click(function () {

        $('.abs-box, .abs-box .center').css('display', 'none');
    });

    $('.abs-box .employe .fa-close').click(function () {

        $('.abs-box, .abs-box .employe').css('display', 'none');
    });

    $('.abs-box .create-order .fa-close').click(function () {

        $('.abs-box, .abs-box .create-order').css('display', 'none');
    });

    $('.abs-box .appoint .fa-close').click(function () {

        $('.abs-box, .abs-box .appoint').css('display', 'none');
    });

    $('.dashboard-table .table-info .file-addbtn').click(function () {

        $('.abs-box .create-order').css('display', 'inline-block');
        $('.abs-box').css('display', 'flex');
    });

    $('.dashboard-table .inner-tr .person-box .file-addbtn').click(function () {

        $('.abs-box .appoint').css('display', 'inline-block');
        $('.abs-box').css('display', 'flex');
    });
});
