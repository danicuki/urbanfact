class MapController < InheritedResources::Base

	def index
		@facts = Fact.find(:all, :conditions => {:hash_tag => I18n.t("site.hashtag")})
	end

end
