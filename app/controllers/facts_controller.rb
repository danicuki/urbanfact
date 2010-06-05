class FactsController < InheritedResources::Base

	def index
		order = params[:order] || "timestamp desc"
		@facts = Fact.all(:order => order)
	end

	def good
		vote 1
	end
	
	def bad
		vote -1
	end
	
	def show
		super do |format|
			@metadata = Metadata.new
    end
	end
	
	private 
	def vote qtd
		@facts = Fact.all
		@fact = Fact.find(params[:fact_id])
		@fact.score = @fact.score + qtd
		@fact.save
		redirect_to :facts
	end
end
