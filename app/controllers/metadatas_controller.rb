class MetadatasController  < InheritedResources::Base
	belongs_to :fact
	
	def create
		super do |format|
      format.html { redirect_to @metadata.fact }
    end
	end
end
