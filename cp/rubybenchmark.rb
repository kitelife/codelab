require 'benchmark'

n = 100000
Benchmark.bm { |x|
	x.report("gsub") {
		for i in 1..n
			a = "abcd\nef" * 10
			b = a.gsub(/\n/," ")
		end
	}
	x.report(" tr"){
		for i in 1..n
			a = "a\nbcd\nef" * 10
			b = a.tr("\n"," ")
		end
	}
}

Benchmark.bm { |b|
	b.report("+= "){
		a = ""
		100000.times{ a += "foo"}
	}
	b.report("<< "){
		a = ""
		100000.times{ a << "foo"}
	}
}
