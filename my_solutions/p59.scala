/***
scalaVersion := "2.11.7"
*/

import scala.io.Source._

val alphRange = 0 to 25
val keyCand: List[List[Char]] = alphRange.map(x=> ('a'.toInt+x).toChar)
	.flatMap(c => alphRange.map(x=> c::('a'.toInt+x).toChar::Nil))
	.flatMap(c => alphRange.map(x=> c(0)::c(1)::('a'.toInt+x).toChar::Nil)).toList

val src = fromFile("../data/cipher.txt")
val lineVal = src.mkString.split(",").map(c=>c.trim.toInt)

def xorForIndex(x: Tuple2[Int, Int], key: List[Char]): Char = x match {
	case (n,i) => (n^key(i%3)).toChar
}

def decryptAndFilter(key:List[Char], lineVal:Array[Int]): String = {
	val decryptedLine = lineVal.zipWithIndex.map(x => xorForIndex(x, key))
	if (countChar(decryptedLine, 'e') > 100)
		key.mkString(",") + decryptedLine.mkString("") + "\n\n"
	else
		""
}

def countChar(toCount:Array[Char], ch: Char): Int = {
	toCount.count(_==ch)
}


println(keyCand.map(key => decryptAndFilter(key, lineVal)).filter(x=> x!=""))

val answer = lineVal.zipWithIndex.map(v => xorForIndex(v, "god".toList).toInt).sum
println(answer)

