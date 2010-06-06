class ChangeLatLngToFloat < ActiveRecord::Migration
  def self.up
    change_table :facts do |t|
      t.change :lat, :Float
      t.change :lng, :Float
    end
  end

  def self.down
  	raise ActiveRecord::IrreversibleMigration
  end
end
