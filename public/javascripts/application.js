// Place your application-specific JavaScript functions and classes here
// This file is automatically included by javascript_include_tag :defaults
// $(document).ready(function(){
// 	$("#good").click(function() {
// 		alert("oi");
// 		return false;
// 	});
// });

$(document).ready(function(){
    // Uses the new live method in jQuery 1.3+
    $('#vote_link').live('click', function(event) {
            $.ajax({
				beforeSend: function() {
					// alert($(event.target).parent().get(0).href);
				},
                url: $(event.target).parent().get(0).href,
                type: 'get',
                dataType: 'script',
                data: { '_method': 'get' },
                success: function(response) {
					resp = eval('(' + response + ')');
                    $('#fact_' + resp.fact.id + '_score').html(resp.fact.score);
                }
            });
        return false;
    });
});
