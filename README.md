# Información sobre los casos de coronavirus en España

**_Última actualización: 03-04-2020_**

* Número de casos: **117.710**
* Número de curados: **30.513**
* Número de fallecidos: **10.935**
* Número de hospitalizados: **56.637**
* Número de ingresados en UCI: **6.416**

En este repositorio se ha recopilado la información otorgada diariamente por el Ministerio de Sanidad de españa sobre los casos de coronavirus en las diferentes comunidades autónomas. La información recopilada consiste en el número de casos total, número de casos nuevos, número de fallecimientos y número de ingresos en UCI por cada comunidad autónoma.

## Frecuencia de actualización

La frecuencia de actualización está sujeta a la frecuencia con la que el ministerio de sanidad publique sus informes, dado que en ocasiones, no han actualizado los datos de forma diaria.

## Descripción de los datos

Se presentan los datos por día y por comunidad autónoma. En caso de que el valor sea 'null', significa que el ministerio no reportaba en ese momento ese tipo de dato, como ocurre en el caso de hospitalizaciones para fechas anteriores a 2020-03-21.

Por cada día tenemos:
 * _TotalCasos:_ Número total de casos en España (Acumulativo).
 * _TotalCasosNuevos:_ Número total de casos ese día concreto en España (No acumulativo).
 * _TotalIngresosUCI:_ Número total de ingresos en UCI en España (Acumulativo).
 * _TotalIngresosUCINuevos:_ Número total de ingresos ese día concreto en UCI en España (No acumulativo).
 * _TotalFallecidos:_ Número total de fallecidos en España (Acumulativo).
 * _TotalFallecidosNuevos:_ Número total de fallecidos ese día concreto en España (No acumulativo).
 * _TotalCurados:_ Número total de curados (Altas) en España (Acumulativo).
 * _TotalCuradosNuevos:_ Número total de curados (Altas) ese día concreto en España (No acumulativo).
 * _TotalHospitalizados:_ Número total de hospitalizaciones (Incluyendo UCI) en España (Acumulativo).
 * _TotalHospitalizadosNuevos:_ Número total de hospitalizaciones (Incluyendo UCI) ese día concreto en España (No acumulativo).

Por cada comunidad autónoma tenemos:
 * _Nombre:_ Nombre de la comunidad autónoma.
 * _Latitud:_ Latitud en grados de la comunidad autónoma.
 * _Longitud:_ Longitud en grados de la comunidad autónoma.
 * _Casos:_ Número de casos en la comunidad autónoma (Acumulativo).
 * _CasosNuevos:_ Número de casos ese día concreto en la comunidad autónoma (No acumulativo).
 * _Curados:_ Número de curados (Altas) en la comunidad autónoma (Acumulativo).
 * _CuradosNuevos:_ Número de curados (Altas) ese día concreto en la comunidad autónoma (No acumulativo).
 * _Fallecidos:_ Número de fallecidos en la comunidad autónoma (Acumulativo).
 * _FallecidosNuevos:_ Número de fallecidos ese día concreto en la comunidad autónoma (No acumulativo).
 * _Hospitalizados:_ Número de hospitalizados (Incluyendo UCI) en la comunidad autónoma (Acumulativo).
 * _HospitalizadosNuevos:_ Número de hospitalizados (Incluyendo UCI) ese día concreto en la comunidad autónoma (No acumulativo).
 * _IngresosUCI:_ Número de ingresos en UCI en la comunidad autónoma (Acumulativo).
 * _IngresosUCINuevos:_ Número de ingresos en UCI ese día concreto en la comunidad autónoma (No acumulativo).

## Veracidad de los datos

Revisando cada uno de los informes diarios publicados por el Ministerio de Sanidad español, he encontrado algunas irregularidades en los mismos. He intentado plasmar aquí con la mayor veracidad posible los datos publicados por el ministerio de sanidad. Si hay algún error o irregularidades en los datos, sería conveniente abrir una Issue en este repositorio para arreglarlo lo antes posible.

## Reconocimiento

Si utilizas, analizas o procesas estos datos, ya sea total o parcialmente, para la obtención o publicación de resultados o de los mismos datos en algún tipo de artículo documento o escrito, incluye el siguiente texto:

***Datos recopilados por Alberto Casas Ortiz (www.albertocasasortiz.com) a partir de los informes publicados por el Ministerio de Sanidad español.***

## Fuente

Informes liberados diariamente por el ministerio de sanidad español: https://www.mscbs.gob.es/
