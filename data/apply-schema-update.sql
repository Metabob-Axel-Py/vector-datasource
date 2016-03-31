-- update polygon table to add feature zoom levels
ALTER TABLE planet_osm_polygon ADD COLUMN mz_poi_min_zoom REAL;
ALTER TABLE planet_osm_polygon ADD COLUMN mz_landuse_min_zoom REAL;
ALTER TABLE planet_osm_polygon ADD COLUMN mz_transit_level REAL;

-- same for line table
ALTER TABLE planet_osm_line ADD COLUMN mz_road_level SMALLINT;
ALTER TABLE planet_osm_line ADD COLUMN mz_transit_level SMALLINT;

-- same for point
ALTER TABLE planet_osm_point ADD COLUMN mz_poi_min_zoom REAL;

-- and pre-calculated areas for all the polygonal NE and static OSM
-- tables.
ALTER TABLE ne_110m_ocean ADD COLUMN way_area REAL;
ALTER TABLE ne_110m_lakes ADD COLUMN way_area REAL;
ALTER TABLE ne_50m_ocean ADD COLUMN way_area REAL;
ALTER TABLE ne_50m_lakes ADD COLUMN way_area REAL;
ALTER TABLE ne_50m_playas ADD COLUMN way_area REAL;
ALTER TABLE ne_10m_ocean ADD COLUMN way_area REAL;
ALTER TABLE ne_10m_lakes ADD COLUMN way_area REAL;
ALTER TABLE ne_10m_playas ADD COLUMN way_area REAL;
ALTER TABLE ne_10m_urban_areas ADD COLUMN way_area REAL;
ALTER TABLE ne_50m_urban_areas ADD COLUMN way_area REAL;
ALTER TABLE ne_10m_parks_and_protected_lands ADD COLUMN way_area REAL;
ALTER TABLE water_polygons ADD COLUMN way_area REAL;
