class CreateMetadatas < ActiveRecord::Migration
  def self.up
    create_table :metadatas do |t|
      t.text :comment
      t.reference :fact

      t.timestamps
    end
  end

  def self.down
    drop_table :metadatas
  end
end
