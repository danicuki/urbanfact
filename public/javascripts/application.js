
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
					$('#fact_' + resp.fact.id + '_score').removeClass("score_good");
					$('#fact_' + resp.fact.id + '_score').removeClass("score_bad");
					$('#fact_' + resp.fact.id + '_score').removeClass("score_neutral");
					$('#fact_' + resp.fact.id + '_score').addClass("score_" + resp.fact.score_kind);
                }
            });
        return false;
    });
});
