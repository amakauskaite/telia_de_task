-- Have all the tables in one data set. Alternatevily, this part of code could be used to create a view (or temporary table) and then it could be used instead in the following queries. 
SELECT A.[site], A.[year], A.[month], A.[day], A.[cell_identity], A.[frequency_band], B.[site_id]
FROM (             
        SELECT 'gsm' as [site], [year], [month], [day], [cell_identity], [frequency_band], [site_id]
        FROM gsm
    UNION ALL
        SELECT 'lte' as [site], [year], [month], [day], [cell_identity], [frequency_band], [site_id]
        FROM lte
    UNION ALL
        SELECT 'umts' as [site], [year], [month], [day], [cell_identity], [frequency_band], [site_id]
        FROM umts 
        ) A
    LEFT JOIN site B ON A.site_id = B.site_id

-- How many cells per technology are there on each site.
SELECT B.[site_id], COUNT(CASE [site] WHEN 'lte' THEN [cell_identity] END) AS site_lte_cnt, COUNT(CASE [site] WHEN 'umts' THEN [cell_identity] END) AS site_umts_cnt, COUNT(CASE [site] WHEN 'gsm' THEN [cell_identity] END) AS site_gsm_cnt
FROM (             
        SELECT 'gsm' as [site], [year], [month], [day], [cell_identity], [frequency_band], [site_id]
        FROM gsm
    UNION ALL
        SELECT 'lte' as [site], [year], [month], [day], [cell_identity], [frequency_band], [site_id]
        FROM lte
    UNION ALL
        SELECT 'umts' as [site], [year], [month], [day], [cell_identity], [frequency_band], [site_id]
        FROM umts 
        ) A
    LEFT JOIN site B ON A.site_id = B.site_id
GROUP BY B.[site_id]

-- Calculate number of cells per frequency band on a particular site
SELECT B.[site_id], 'frequency_band_' || CAST([frequency_band] AS INTEGER) || '_by_site' AS frequency_band_by_site, COUNT(*) as cnt
FROM (             
        SELECT 'gsm' as [site], [year], [month], [day], [cell_identity], [frequency_band], [site_id]
        FROM gsm
    UNION ALL
        SELECT 'lte' as [site], [year], [month], [day], [cell_identity], [frequency_band], [site_id]
        FROM lte
    UNION ALL
        SELECT 'umts' as [site], [year], [month], [day], [cell_identity], [frequency_band], [site_id]
        FROM umts 
        ) A
    LEFT JOIN site B ON A.site_id = B.site_id
GROUP BY B.[site_id], 'frequency_band_' || CAST([frequency_band] AS INTEGER) || '_by_site'