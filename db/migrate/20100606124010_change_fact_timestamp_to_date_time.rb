class ChangeFactTimestampToDateTime < ActiveRecord::Migration
  def self.up
	  change_table :facts do |t|
      t.change :timestamp, :datetime
			t.change :score, :integer, :null => false
    end
  end

  def self.down
	  change_table :facts do |t|
      t.change :timestamp, :date
    end
  end
end
