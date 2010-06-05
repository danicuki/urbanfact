class FactsController < InheritedResources::Base

	def good
		vote 1
	end
	
	def bad
		vote -1
	end
	
	private 
	def vote qtd
		@facts = Fact.all
		@fact = Fact.find(params[:fact_id])
		@fact.score = @fact.score + qtd
		@fact.save
		render :index
	end
end
