class MapController < InheritedResources::Base

	def index
		@facts = Fact.all()
	end

end
