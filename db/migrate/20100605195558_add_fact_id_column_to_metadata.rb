class AddFactIdColumnToMetadata < ActiveRecord::Migration
  def self.up
		add_column :metadatas, :fact_id, :integer
  end

  def self.down
		remove_column :metadatas, :fact_id
  end
end
