class FactsController < InheritedResources::Base

	def index
		order = params[:order] || "timestamp desc"
		@facts = Fact.find(:all, :conditions => {:hash_tag => I18n.t("site.hashtag")}, :order => order)
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
		respond_to do |format|
        format.html { redirect_to :facts }
        format.js { render :json => {:fact => {:score_kind => @fact.score_kind}.merge(@fact.attributes)}	 }
    end
    
	end
end
