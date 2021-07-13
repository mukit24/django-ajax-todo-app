$(document).ready(function(){
    $('tbody').on('click','#edit_btn',function(e){
        e.preventDefault();
        $('.notification .alert').hide();
        let id = $(this).attr('data-sid');
        console.log(id);
        let status = $(this).parent().siblings('#task_status').text();
        let name = $(this).parent().siblings('#task_name').text();
        console.log(status);
    
        $('.add_task h4').text('Edit Task');
        $('#edit_task_btn').show();
        $('#create_task_btn').hide();
        $('#id_input').val(id);
        $('#id_name').val(name);
        $('#id_status').val(status);
    })
    
    $('#refresh_btn').click(function(e){
        e.preventDefault();
        window.location.reload();
    })
    
    // $('#refresh_btn').click(function(e){
    //     e.preventDefault();
    //     console.log('yoooo');
    // });
});