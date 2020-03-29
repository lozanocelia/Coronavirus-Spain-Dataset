# Información sobre los casos de coronavirus en España

_Última actualización: 29-03-2020_

* Número de casos: 78.797
* Número de curados: 14.709
* Número de fallecidos: 6.528
* Número de hospitalizados: 43.397
* Número de ingresados en UCI: 4.907

En este repositorio se ha recopilado la información otorgada diariamente por el Ministerio de Sanidad de españa sobre los casos de coronavirus en las diferentes comunidades autónomas. La información recopilada consiste en el número de casos total, número de casos nuevos, número de fallecimientos y número de ingresos en UCI por cada comunidad autónoma.

## Frecuencia de actualización

La frecuencia de actualización está sujeta a la frecuencia con la que el ministerio de sanidad publique sus informes, dado que en ocasiones, no han actualizado los datos de forma diaria.

## Descripción de los datos

Se presentan los datos por día y por comunidad autónoma. En caso de que el valor sea 'null', significa que el ministerio no reportaba en ese momento ese tipo de dato, como ocurre en el caso de hospitalizaciones para fechas anteriores a 2020-03-21.

Por cada día tenemos:
 * TotalCasos: Número total de casos en España (Acumulativo).
 * TotalCasosNuevos: Número total de casos ese día concreto en España (No acumulativo).
 * TotalIngresosUCI: Número total de ingresos en UCI en España (Acumulativo).
 * TotalIngresosUCINuevos: Número total de ingresos ese día concreto en UCI en España (No acumulativo).
 * TotalFallecidos: Número total de fallecidos en España (Acumulativo).
 * TotalFallecidosNuevos: Número total de fallecidos ese día concreto en España (No acumulativo).
 * TotalCurados: Número total de curados (Altas) en España (Acumulativo).
 * TotalCuradosNuevos: Número total de curados (Altas) ese día concreto en España (No acumulativo).
 * TotalHospitalizados: Número total de hospitalizaciones (Incluyendo UCI) en España (Acumulativo).
 * TotalHospitalizadosNuevos: Número total de hospitalizaciones (Incluyendo UCI) ese día concreto en España (No acumulativo).

Por cada comunidad autónoma tenemos:
 * Nombre: Nombre de la comunidad autónoma.
 * Latitud: Latitud en grados de la comunidad autónoma.
 * Longitud: Longitud en grados de la comunidad autónoma.
 * Casos: Número de casos en la comunidad autónoma (Acumulativo).
 * CasosNuevos: Número de casos ese día concreto en la comunidad autónoma (No acumulativo).
 * Curados: Número de curados (Altas) en la comunidad autónoma (Acumulativo).
 * CuradosNuevos: Número de curados (Altas) ese día concreto en la comunidad autónoma (No acumulativo).
 * Fallecidos: Número de fallecidos en la comunidad autónoma (Acumulativo).
 * FallecidosNuevos: Número de fallecidos ese día concreto en la comunidad autónoma (No acumulativo).
 * Hospitalizados: Número de hospitalizados (Incluyendo UCI) en la comunidad autónoma (Acumulativo).
 * HospitalizadosNuevos: Número de hospitalizados (Incluyendo UCI) ese día concreto en la comunidad autónoma (No acumulativo).
 * IngresosUCI: Número de ingresos en UCI en la comunidad autónoma (Acumulativo).
 * IngresosUCINuevos: Número de ingresos en UCI ese día concreto en la comunidad autónoma (No acumulativo).

## Veracidad de los datos

Revisando cada uno de los informes diarios publicados por el Ministerio de Sanidad español, he encontrado algunas irregularidades en los mismos. He intentado plasmar aquí con la mayor veracidad posible los datos publicados por el ministerio de sanidad. Si hay algún error o irregularidades en los datos, sería conveniente abrir una Issue en este repositorio para arreglarlo lo antes posible.

## Reconocimiento

Si utilizas, analizas o procesas estos datos, ya sea total o parcialmente, para la obtención o publicación de resultados o de los mismos datos en algún tipo de artículo documento o escrito, incluye el siguiente texto:

***Datos recopilados por Alberto Casas Ortiz (www.albertocasasortiz.com) a partir de los informes publicados por el Ministerio de Sanidad español.***

## Fuente

Informes liberados diariamente por el ministerio de sanidad español: https://www.mscbs.gob.es/
