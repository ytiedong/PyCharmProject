import pyodbc
from django.db import connection

from sales.common import as400connection


def uriagesql():
    c1 = as400connection.as400connection()
    c1.execute('''SELECT
      CASE
        WHEN U.UTRN15 = '50'
        THEN '4.OS'
        WHEN
      LEFT (P1.SEIK01, 1) = '3'
      THEN '3.MI'
      WHEN U.UTRN05 IN (' 3', '37', '38', '39')
      THEN '2.OF'
      WHEN U.UTRN05 IN (
        ' 1'
        , '17'
        , '18'
        , '19'
        , ' 2'
        , '27'
        , '28'
        , '29'
        , ' 4'
        , '47'
        , '48'
        , '49'
      )
      THEN '1.OG'
      ELSE '9.その他'
      END AS BUMON
      , CASE
      WHEN U.UTRN05 LIKE '1_'
      OR U.UTRN05 LIKE '2_'
      OR U.UTRN05 LIKE '3_'
      OR U.UTRN05 LIKE '4_'
      THEN '返品等'
      WHEN U.UTRN05 IN (' 1', ' 2', ' 3', ' 4', ' 5', ' 6')
      THEN '売上'
      ELSE 'その他'
      END AS SEIKBN
      , CASE
      WHEN P2.SEIK01 IS NOT NULL
      THEN TRIM(P2.SEIK02)
      WHEN P1.SEIK01 IS NOT NULL
      THEN TRIM(P1.SEIK02)
      WHEN UTRN15 = '50'
      THEN 'OSその他(PG未指定)'
      WHEN GW.GWO01 IS NOT NULL
      THEN 'OGその他(PG未設定)'
      WHEN U.UTRN05 IN (
        ' 1'
        , '17'
        , '18'
        , '19'
        , ' 2'
        , '27'
        , '28'
        , '29'
        , ' 4'
        , '47'
        , '48'
        , '49'
      )
      THEN 'OGその他(P未設定)'
      WHEN U.UTRN05 IN (' 5', '57', '58', '59')
      THEN 'その他(売上商品)'
      WHEN U.UTRN05 IN (' 6', '67', '68', '69')
      THEN 'その他(その他)'
      WHEN
      LEFT (P1.SEIK01, 1) = '3'
      THEN 'MIその他'
      WHEN U.UTRN05 IN (' 3', '37', '38', '39')
      THEN 'OFその他(その他)'
      ELSE 'その他'
      END AS PG
      , CASE
      WHEN GW.GWO01 IS NOT NULL
      THEN TRIM(GW.GWO02)
      WHEN P1.SEIK01 IS NOT NULL
      AND P2.SEIK01 IS NULL
      THEN TRIM(S.SID04)
      WHEN P1.SEIK01 IS NOT NULL
      THEN TRIM(P1.SEIK02)
      WHEN U.UTRN05 IN (' 6', '67', '68', '69')
      THEN '-'
      WHEN U.UTRN05 IN (' 5', '57', '58', '59')
      THEN '-'
      WHEN U.UTRN05 IN (' 4', '47', '48', '49')
      THEN 'ルミラス等'
      WHEN U.UTRN05 IN (' 1', '17', '18', '19')
      AND GWO02 IS NULL
      THEN 'その他原塊'
      WHEN U.UTRN05 IN (' 2', '27', '28', '29')
      AND GWO02 IS NULL
      THEN 'その他ガラス'
      ELSE 'その他(指定なし)'
      END AS P
      , CASE
      WHEN P2.SEIK01 IS NULL
      THEN '-'
      WHEN U.UTRN05 NOT IN (' 3', '37', '38', '39')
      THEN '-'
      WHEN S.SID03 IS NOT NULL
      THEN TRIM(S.SID04)
      END AS PS
      , K.TCORD1
      , CASE
      WHEN K.TOKNM2 = ''
      THEN TRIM(CONCAT(U.UTRN03, '_'))
      ELSE TRIM(K.TOKNM2)
      END AS TOKUI_NAME
      , K.RNAME1
      , U.UTRN01
      , U.UTRN02
      , U.UTRN10
      , U.UTRN11
      , U.UTRN12
      , CASE
      WHEN UTRN05 > 6
      THEN NULL
      WHEN G.GEN03 IS NULL
      THEN SI.GENKA4
      ELSE G.GEN03
      END AS GENKA
      , CASE
      WHEN UTRN05 > 6
      THEN NULL
      WHEN G.GEN03 IS NULL
      THEN SI.GENKA4
      ELSE G.GEN03
      END * U.UTRN10 AS SEIKIN
      , U.UTRN09
      , U.UTRN03
      , U.UTRN06
      , case
      when U.UTRN16 = ''
      then '00'
      else U.UTRN16
      end U16
      , EI.EIG05
      , case
      when K.TANCD1 = '44'
      then '海外'
      else '国内'
      end AS OVERSEA
      , case
      when K.TANCD1 = '44'
      then trim(K.TANT1)
      else '日本'
      end AS AREA
      , case
      when K.TCORD1 = '1607'
      then '住田東莞'
      when K.TANCD1 = '44'
      AND trim(K.TANT2) = '中国'
      then '中国'
      when K.TANCD1 = '44'
      AND trim(K.TANT2) = '台湾'
      then '台湾'
      when K.TANCD1 = '44'
      AND trim(K.TANT2) = '韓国'
      then '韓国'
      when K.TANCD1 = '44'
      AND trim(K.TANT2) IN (
        'シンガポール'
        , 'タイ'
        , 'フィリピン'
        , 'ベトナム'
        , 'マレーシア'
        , 'インドネシア'
        , 'カンボジア'
        , 'ブルネイ'
        , 'ミャンマー'
        , 'ラオス'
      )
      then 'ASEAN'
      when K.TANCD1 = '44'
      AND (
        trim(K.TANT1) = 'アジア'
        OR trim(K.TANT1) = 'オセアニア'
      )
      then 'その他アジア'
      when K.TANCD1 = '44'
      then trim(K.TANT1)
      else '日本'
      end AS AREA2
      , case
      when K.TANCD1 = '44'
      then trim(K.TANT2)
      else '日本'
      end AS COUNTRY
      , int ((UTRN09 - 19510900) / 10000) || '期' as KI
      , CASE
      WHEN int (SUBSTR(UTRN09, 5, 2)) > 2
      AND int (SUBSTR(UTRN09, 5, 2)) < 9
      THEN '下期'
      ELSE '上期'
      END AS URIKAMISIMO
      , CASE
      WHEN int (SUBSTR(UTRN09, 5, 2)) > 8
      AND int (SUBSTR(UTRN09, 5, 2)) < 12
      THEN '1Q'
      WHEN int (SUBSTR(UTRN09, 5, 2)) > 2
      AND int (SUBSTR(UTRN09, 5, 2)) < 6
      THEN '3Q'
      WHEN int (SUBSTR(UTRN09, 5, 2)) > 5
      AND int (SUBSTR(UTRN09, 5, 2)) < 9
      THEN '4Q'
      ELSE '2Q'
      END AS URIQ
      , substring(UTRN09, 1, 4) || '/' || substring(UTRN09, 5, 2) as YYYYMM
      , U.UTRN05 AS U05
      , CASE
      WHEN A.ACCE09 IS NOT NULL
      AND U.UTRN15 <> A.ACCE09
      THEN A.ACCE09
      ELSE U.UTRN15
      END AS U15
      , GW.GWO01
      , CASE
      WHEN UTRN15 = '50'
      AND GWO02 IS NOT NULL
      THEN TRIM(GWO02)
      WHEN UTRN15 = '50'
      THEN 'その他光システム'
      WHEN U.UTRN05 IN (' 4', '47', '48', '49')
      THEN 'ルミラス等'
      WHEN U.UTRN05 IN (' 5', '57', '58', '59')
      THEN '売上商品'
      WHEN U.UTRN05 IN (' 6', '67', '68', '69')
      THEN 'その他'
      WHEN U.UTRN05 IN (' 3', '37', '38', '39')
      THEN TRIM(S.SID04)
      WHEN U.UTRN05 IN (' 1', '17', '18', '19')
      AND GWO02 IS NULL
      THEN 'その他原塊'
      WHEN U.UTRN05 IN (' 1', '17', '18', '19')
      THEN TRIM(GWO02)
      WHEN U.UTRN05 IN (' 2', '27', '28', '29')
      AND GWO02 IS NULL
      THEN 'その他ガラス'
      WHEN U.UTRN05 IN (' 2', '27', '28', '29')
      THEN TRIM(GWO02)
      ELSE '※予期せぬ区分名※'
      END AS KBNMEI
      , CASE
      WHEN P2.SEIK01 IS NOT NULL
      THEN P2.SEIK01
      WHEN P1.SEIK01 IS NOT NULL
      THEN P1.SEIK01
      WHEN U.UTRN05 IN (
        ' 1'
        , '17'
        , '18'
        , '19'
        , ' 2'
        , '27'
        , '28'
        , '29'
        , ' 4'
        , '47'
        , '48'
        , '49'
      )
      THEN '(不明)'
      WHEN U.UTRN05 IN (' 5', '57', '58', '59')
      THEN '(不明)'
      WHEN U.UTRN05 IN (' 6', '67', '68', '69')
      THEN '(不明)'
      ELSE 'XXX'
      END AS PG_CODE
      , CASE
      WHEN GW.GWO01 IS NOT NULL
      THEN GW.GWO01
      WHEN P2.SEIK01 IS NOT NULL
      THEN P2.SEIK03
      WHEN P1.SEIK01 IS NOT NULL
      THEN P1.SEIK03
      WHEN U.UTRN05 NOT IN (' 3', '37', '38', '39')
      THEN '(不明)'
      END AS P_CODE
      , CASE
      WHEN P2.SEIK01 IS NULL
      THEN '-'
      WHEN U.UTRN05 NOT IN (' 3', '37', '38', '39')
      THEN '(不明)'
      WHEN S.SID03 IS NOT NULL
      THEN S.SID03
      END AS PS_CODE
    FROM
      YANG_S.URITRAN AS U
      LEFT JOIN YANG_S.URIKAKE AS K
        ON U.UTRN08 = K.TCORD1
      LEFT JOIN YANG_T.ACCEPT00 A
        ON SUBSTR(U.UTRN06, 1, LENGTH(U.UTRN06) - 2) = A.ACCE03
      LEFT JOIN YANG_T.SIDFILE AS S
        ON CASE
          WHEN A.ACCE09 IS NOT NULL
          AND U.UTRN15 <> A.ACCE09
          THEN A.ACCE09
          ELSE U.UTRN15
          END = S.SID03
      LEFT JOIN (
        SELECT
          GEN02
          , MAX(GEN03) AS GEN03
        FROM
          YANG_S.GENKA
        WHERE
          GEN02 <> 0
        GROUP BY
          GEN02
      ) AS G
        ON U.UTRN14 = G.GEN02
      LEFT JOIN YANG_S.SEIHIN AS SI
        ON U.UTRN01 = SI.HINMEI
      LEFT JOIN YANG_S.EIGTAN AS EI
        ON U.UTRN16 = EI.EIG03
      LEFT JOIN YANG_S.GWORK00 AS GW
        ON SI.CLASS4 = GW.GWO01
      LEFT JOIN YANG_S.PGSEIKU P1
        ON (
          S.SID03 = P1.SEIK03
          AND U.UTRN05 IN (' 3', '37', '38', '39')
          OR GW.GWO01 = P1.SEIK03
        )
      LEFT JOIN YANG_S.PGSEIKU P2
        ON P1.SEIK01 = P2.SEIK03
    WHERE
      1 = 1
      AND U.UTRN04 = 0
      AND U.UTRN09 BETWEEN 20201000 AND 20201200
      AND U.UTRN16 = '87'
    ORDER BY
      U.UTRN09
      , BUMON
      , PG_CODE
      , P_CODE
      , PS_CODE
      , K.TOKNM2
      , U.UTRN01
    ''')

    return c1

def testsql():
    c2 = as400connection.db2connection()

    return c2
