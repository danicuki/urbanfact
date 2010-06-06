class Fact < ActiveRecord::Base
	has_many :metadatas
	attr_accessor :score_kind
	def small_description
		return description if description.size <= 20
		"#{description[0..19]}..."
	end
	
	def score_kind
		return :neutral if score == 0
		return :bad if score < 0
	 :good
	end
	
end
