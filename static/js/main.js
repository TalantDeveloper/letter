$(document).ready(function(){
    $('.img-box').css({'height': $(window).height()-$('header').height()-$('.menyu1').height()});
    $('.big-card').css({'height': $(window).height()-$('header').height()-$('.menyu1').height()});
    $('.mini-admin .right-bar form').css({'height': $(window).height()-$('header').height()-100});
    $('header nav').css('width', $('.left-bar').width());

    $('#file').change(function() {
        var filename = $('#file').val();
        var ss = filename.split('\\');
        $('#file-name').text(ss[ss.length-1]);
        $('.added-file').slideDown();
    });
    
    $('.control-btn').click(function(){
        $(this).find('i').removeClass('fa-check').addClass('fa-clock-o');
        $(this).siblings().find('i').removeClass('fa-exclamation').addClass('fa-check');
    })
    $('.srok-control-label').click(function(){
        if($('#srok-control').is(":checked"))
        {
            $('.add-box-srok').slideUp();
        }
        if(!($('#srok-control').is(":checked")))
        {
            $('.add-box-srok').slideDown();
        }
    });
    $('#spismo').click(function(){
        if($('#sopro').is(":checked"))
        {
            $('.spismo-data').slideDown();
            $('#sopro_val').val('on');
        }
        if(!($('#sopro').is(":checked")))
        {
            $('.spismo-data').slideUp();
            $('#sopro_val').val('off');
        }
    });

	$('#select-org_group').click(function(){
    $('.create-select-lists li').css('display', 'block');
		$('.create-select-lists li em').each(function(index, value){
        	if($(this).text() != $('#select-org_group').val()){
            	$(this).parent().css('display', 'none');
            }
		});
    });
 
	$('#tipconcart').click(function(){
			if($(this).val() == "16"){
				$('.1b').css('display','block');
				$('.2b').css('display','none');
				$('.3b').css('display','none');
				$('.4b').css('display','none');
			}
			if($(this).val() == "26"){
			$('.1b').css('display','none');
			$('.2b').css('display','block');
			$('.3b').css('display','none');
			$('.4b').css('display','none');
			}
			if($(this).val() == "36"){
			$('.1b').css('display','none');
			$('.2b').css('display','none');
			$('.3b').css('display','block');
			$('.4b').css('display','none');
			}
			if($(this).val() == "46"){
			$('.1b').css('display','none');
			$('.2b').css('display','none');
			$('.3b').css('display','none');
			$('.4b').css('display','block');
			}
			if($(this).val() == "ТДСИ фуқаролари"){
			$('.1b').css('display','none');
			$('.2b').css('display','none');
			$('.3b').css('display','none');
			$('.4b').css('display','none');
			}
    });

	$('.select-lists input').click(function(){
		$('.select-lists nav').slideToggle();
	});
	$('.select-lists nav li').click(function(){
    	$('.select-lists input').val($(this).find('b').text());
		$('.select-lists nav').css('display', 'none');
	});

    $('#spismo_update').click(function(){
        if($('#update_sopro').is(":checked"))
        {
            $('.spismo-data').slideDown()
        }
        if(!($('#update_sopro').is(":checked")))
        {
            $('.spismo-data').slideUp();
        }
    });
    $('.add-box-ctrl label').click(function(){
        $('.add-box').slideUp();
    });
    $('.person-editor').click(function(){
    	$('.file-box-update').slideDown();
    	$('.main-bar').css('overflow','hidden');
    	$('.main-bar').scrollTop(0);
    	$('#prosta').text($(this).parent().parent().find('.manager_markaz_id').text());
        
        $('#updatenaz_id').val($(this).parent().parent().find('.naz-id').find('input').val());
        $('#updaterez').text($(this).parent().parent().find('.manager_rezolyutsiya').text());
        // $('.updatenaz_markaz').val($(this).parent().parent().find('.manager_markaz_id').text());
    	$(".updatenaz_markaz option:selected" ).text($('#prosta').text());
        $('.updatenaz_xodim').val($(this).parent().parent().find('.manager_xodim_id').text());
        if($(this).parent().find('.status-manager-val').val() == 'on')
        {
            $('#nazctrl').prop( "checked", true );
            $('#nazctrl_val').val('on');
        }
    });
    $('#show-add-box').click(function(){
        $('.file-box').slideDown();
    });
    $('.status-manager').click(function(){
        if($(this).is(':checked'))
        {
            $(this).parent().find('.status-manager-val').val('on');
        }
        else
        {
            $(this).parent().find('.status-manager-val').val('off');
        }
        $('.add-content .manage-status input[type="submit"]').slideDown();
    });
    
    $data_reg = $('#date_reg0').text().split(' ');
    $('#date_reg').val($data_reg[0]+'T'+$data_reg[1]);
    
    $data_doc = $('#date_doc0').text().split(' ');
    $('#date_doc').val($data_doc[0]+'T'+$data_doc[1]);

    $sopro_date = $('#sopro_date0').text().split(' ');
    $('#sopro_date').val($sopro_date[0]+'T'+$sopro_date[1]);

    $srok = $('#srok0').text().split(' ');
    $('#srok').val($srok[0]+'T'+$srok[1]);
    
    $nazsrok = $('#nazsrok0').text().split(' ');
    $('#nazsrok').val($nazsrok[0]+'T'+$nazsrok[1]);

    $nazreg_date = $('#nazreg_date0').text().split(' ');
    $('#nazreg_date').val($nazreg_date[0]+'T'+$nazreg_date[1]);

    $updatenazreg_date = $('#updatenazreg_date0').text().split(' ');
    $('#updatenazreg_date').val($updatenazreg_date[0]+'T'+$updatenazreg_date[1]);

    $updatenazsrok = $('#updatenazsrok0').text().split(' ');
    $('#updatenazsrok').val($updatenazreg_date[0]+'T'+$updatenazreg_date[1]);
    
    $('.dsp').click(function(){
        if($('#dsp').is(":checked"))
        {
            $('#dsp_val').val('on');
        }
        if(!($('#dsp').is(":checked")))
        {
            $('#dsp_val').val('off');
        }
    });
    $('.dsp_update').click(function(){
        if($('#dsp_update').is(":checked"))
        {
            $('#dsp_update_val').val('on');
        }
        if(!($('#dsp_update').is(":checked")))
        {
            $('#dsp_update_val').val('off');
        }
    });
    // povtor
    $('.povtor').click(function(){
        if($('#povtor').is(":checked"))
        {
            $('#povtor_val').val('on');
            $('.povtor-data').slideDown();
        }
        if(!($('#povtor').is(":checked")))
        {
            $(this).val('off');
            $('.povtor-data').slideUp();
        }
    });
    $('.povtor_update').click(function(){
        if($('#update_povtor').is(":checked"))
        {
            $('#update_povtor_val').val('on');
            $('.povtor-data').slideDown();
        }
        if(!($('#update_povtor').is(":checked")))
        {
            $('#update_povtor_val').val('off');
            $('.povtor-data').slideUp();
        }
    });

    $('.controlnoe').click(function(){
        if($('#controlnoe').is(":checked"))
        {
            $('#controlnoe_val').val('on');
        }
        if(!($('#controlnoe').is(":checked")))
        {
            $('#controlnoe_val').val('off');
        }
    });
    $('.controlnoe_update').click(function(){
        if($('#update_controlnoe').is(":checked"))
        {
            $('#update_controlnoe_val').val('on');
        }
        if(!($('#update_controlnoe').is(":checked")))
        {
            $('#update_controlnoe_val').val('off');
        }
    });
    $('.nazctrl').click(function(){
        if($('#nazctrl').is(":checked"))
        {
            $('#nazctrl_val').val('on');
        }
        if(!($('#nazctrl').is(":checked")))
        {
            $('#nazctrl_val').val('off');
        }
    });

    $('.order-remover').click(function(){
        $('.delete-order').slideDown();
        $('#delete_id').val($(this).parent().parent().find('.td-id').text());
    });

    $('.markaz-section tr:not(:first-child)').click(function(){
        $('.markaz-save').css('display', 'none');
    	$('.markaz-delete').css('display', 'none');
    	$('.markaz-update').css('display', 'block');
    
    	$('.markaz-delete .delmarkaz-id').val($(this).find('td:nth-child(1)').text());
    	$('.markaz-update .upmarkaz-id').val($(this).find('td:nth-child(1)').text());
    	$('.markaz-delete .delmarkaz-name').text($(this).find('td:nth-child(2)').text());
    	$('.markaz-update .upmarkaz-name').val($(this).find('td:nth-child(2)').text());
    });

    $('.markaz-section .markaz-update .otmenbtn').click(function(){
        $('.markaz-save').css('display', 'block');
    	$('.markaz-delete').css('display', 'none');
    	$('.markaz-update').css('display', 'none');
    });

    $('.markaz-section .markaz-update .delbtn').click(function(){
        $('.markaz-save').css('display', 'none');
    	$('.markaz-delete').css('display', 'block');
    	$('.markaz-update').css('display', 'none');
    });

    $('.markaz-section .markaz-delete .otmenbtn').click(function(){
        $('.markaz-save').css('display', 'none');
    	$('.markaz-delete').css('display', 'none');
    	$('.markaz-update').css('display', 'block');
    });
});